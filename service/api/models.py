from django.contrib.auth.models import User
from django.db import models


class Apartment(models.Model):
    id = models.CharField(primary_key=True, max_length=10)

    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    street_number = models.CharField(max_length=16)
    rooms = models.IntegerField()
    floor = models.IntegerField()
    area = models.IntegerField()
    rent = models.IntegerField()

    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    description = models.TextField()

    def can_read(self, user):
        return True

    def can_update(self, user):
        return True

    def can_delete(self, user):
        return True

    def can_create(self, user):
        return True


def user_can_read(self, user):
    return True


def user_can_update(self, user):
    return self == user


def user_can_delete(self, user):
    return user.is_staff


def user_can_create(self, user):
    return user.is_staff


User.can_read = user_can_read
User.can_update = user_can_update
User.can_delete = user_can_delete
User.can_create = user_can_create

