
# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class BookingPlace(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Zone(models.Model):
    name = models.CharField(max_length=255)
    place_type = models.CharField(max_length=50, choices=[('cafe', 'Кафе'), ('cabin', 'Кабинка')])

    def __str__(self):
        return f"{self.place_type} - {self.name}"

class Event(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    client_name = models.CharField(max_length=255)
    booking_places = models.ManyToManyField(BookingPlace)
    phone_number = PhoneNumberField(unique=True)
    guests_count = models.PositiveIntegerField()
    menu_available = models.BooleanField(default=False)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    place_type = models.CharField(max_length=50, choices=[('restaurant', 'Ресторан'), ('cafe', 'Кафе'), ('cabin', 'Кабинка')])
    zones = models.ManyToManyField(Zone,blank=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.date}"
