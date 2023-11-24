from django.shortcuts import render
from rest_framework import viewsets
from .models import BookingPlace, Zone, Event
from .serializers import BookingPlaceSerializer, ZoneSerializer, EventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, filters
from .filter import EventFilter
from django_filters import rest_framework as dj_filters
from datetime import datetime

class BookingPlaceViewSet(viewsets.ModelViewSet):
    queryset = BookingPlace.objects.all()
    serializer_class = BookingPlaceSerializer

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (dj_filters.DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter)
    filterset_class = EventFilter 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['booking_places'] = BookingPlaceSerializer(instance.booking_places.all(), many=True).data
        representation['zones'] = ZoneSerializer(instance.zones.all(), many=True).data
        return representation

    @action(detail=False, methods=['GET'])
    def events_on_date(self, request):
        date_str = self.request.query_params.get('date', None)
        place_type = self.request.query_params.get('place_type', None)

        if date_str:
            try:
                date = datetime.strptime(date_str, '%d-%m-%Y').date()
                events = Event.objects.filter(date=date)

                if place_type:
                    events = events.filter(place_type=place_type)

                serializer = self.get_serializer(events, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response({'error': 'Invalid date format. Use DD-MM-YYYY.'}, status=400)
        else:
            return Response({'error': 'Date parameter is required.'}, status=400)
