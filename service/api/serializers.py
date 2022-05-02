from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from . import models


class ApartmentSerializer(ModelSerializer):

    class Meta:
        model = models.Apartment
        fields = (
            'id',
            'street',
            'street_number',
            'city',
            'rent',
            'latitude',
            'longitude',
        )
