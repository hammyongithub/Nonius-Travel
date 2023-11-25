from django.contrib import admin
from django.urls import path, include

from nonius_travel import views


urlpatterns = [
    path('latestclients/', views.LatestClientsList.as_view()),
    path('hotelsearch/', views.hotel_search, name='hotelsearch'),
    path('offersearch/', views.offer_search, name='offersearch'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
] 