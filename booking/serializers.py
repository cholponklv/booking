# serializers.py
from rest_framework import serializers
from .models import BookingPlace, Zone, Event

class BookingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPlace
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['booking_places'] = BookingPlaceSerializer(instance.booking_places.all(), many=True).data
        representation['zones'] = ZoneSerializer(instance.zones.all(), many=True).data
        return representation
