from venv import logger
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clients
from .serializers import ClientsSerializer
from django.http import JsonResponse
from .search import search_hotels, search_offers
import logging

logger = logging.getLogger(__name__)

class LatestClientsList(APIView):
    def get(self, request, format=None):
        clients = Clients.objects.all().order_by('-created_at')[:10]
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)

def hotel_search(request):
    location = request.GET.get('location')

    results = search_hotels(location)
    if results:
        return JsonResponse(results)
    else:
        return JsonResponse({'error': 'Failed to fetch hotel data'}, status=500)
    
def offer_search(request):
    try:
        hotelIds = request.GET.get('hotelIds')
        adults = request.GET.get('adults')
        checkInDate = request.GET.get('checkInDate')
        checkOutDate = request.GET.get('checkOutDate')
        roomQuantity = request.GET.get('roomQuantity')
        priceRange = request.GET.get('priceRange')
        currency = request.GET.get('currency')
        boardType = request.GET.get('boardType')

        results = search_offers(hotelIds, adults, checkInDate, checkOutDate, roomQuantity, priceRange, currency, boardType)
        if results:
            return JsonResponse(results)
        else:
            return JsonResponse({'error': 'Failed to fetch offer data'}, status=500)
    except Exception as e:
        logger.error(f"Error in offer_searcg: {e}", exc_info=True)
        return JsonResponse({'error': 'Internal server error'}, status=500)