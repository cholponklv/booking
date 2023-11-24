# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingPlaceViewSet, ZoneViewSet, EventViewSet

router = DefaultRouter()
router.register(r'places', BookingPlaceViewSet, basename='booking-place')
router.register(r'zones', ZoneViewSet, basename='zone')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
