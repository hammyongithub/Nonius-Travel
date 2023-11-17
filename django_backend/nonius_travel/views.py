from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clients
from .serializers import ClientsSerializer
from django.http import JsonResponse
from .search import search_hotels

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