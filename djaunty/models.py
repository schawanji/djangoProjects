from django.db import models
import datetime

# Create your models here.
BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00


class Bike(models.Model):
    ELECTRIC = 'EL'
    STANDARD = 'ST'
    TANDEM = 'TA'
    BIKE_TYPE_CHOICES = [
        (STANDARD, 'standard'),
        (TANDEM, 'tandem'),
        (ELECTRIC, 'electric')
    ]
    bike_type = models.CharField(
        max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    color = models.CharField(max_length=2, default='')

    # Get more info from our model
    def __str__(self):
        return self.bike_type + '-' + self.color


class Renter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    vip_num = models.IntegerField(default=0)
    # Get more info from our model

    def __str__(self):
        return self.first_name + '-' + self.phone


class Rentals(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0.0)

    def price(self):
        if self.bike.bike_type == 'ST':
            current_price = BASE_PRICE
        elif self.bike.bike_type == 'TA':
            current_price += TANDEM_SURCHARGE
        elif self.bike.bike_type == 'EL':
            current_price += ELECTRIC_SURCHARGE
        elif self.renter.vip_num > 0:
            current_price *= 0.8
        self.current_price = current_price
     # Get more info from our model

    def __str__(self):
        return self.renter + '_' + self.bike + '_' + self.date + '_' + self.price
