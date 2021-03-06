from django.contrib.auth.models import User
from django.db import models


class Apartment(models.Model):
    id = models.CharField(primary_key=True, max_length=10)

    building = models.ForeignKey('Building', blank=True, null=True, related_name='apartments', on_delete=models.CASCADE)

    rooms = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    rent = models.IntegerField()

    description = models.TextField()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return True

    def can_delete(self, user):
        return True

    def can_create(self, user):
        return True


class Building(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)

    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    description = models.TextField()

    class Meta:
        unique_together = ('city', 'street', 'street_number')

    def can_read(self, user):
        return True

    def can_update(self, user):
        return True

    def can_delete(self, user):
        return True

    def can_create(self, user):
        return True


class RentalAgreement(models.Model):
    apartment = models.ForeignKey('Apartment', related_name='rental_contracts', on_delete=models.PROTECT)
    tenant = models.ForeignKey(User, related_name='rental_contracts', on_delete=models.PROTECT)

    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(default=None, blank=True, null=True)

    def can_create(self, user):
        return True

    def can_read(self, user):
        return True