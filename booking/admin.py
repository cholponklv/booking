# admin.py
from django.contrib import admin
from .models import BookingPlace, Zone, Event

@admin.register(BookingPlace)
class BookingPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_type')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'date', 'start_time', 'place_type')
    search_fields = ('cleint_name', 'date', 'start_time')
    list_filter = ('place_type', 'zones')
