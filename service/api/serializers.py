from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from . import models


class ApartmentSerializer(ModelSerializer):

    class Meta:
        model = models.Apartment
        fields = (
            'id',
            'building',
            'rent',
            'rooms',
            'floor',
            'area',
        )


class BuildingSerializer(ModelSerializer):

    class Meta:
        model = models.Building
        fields = (
            'id',
            'street',
            'street_number',
            'city',
            'latitude',
            'longitude',
        )


class RentalAgreementSerializer(ModelSerializer):

    class Meta:
        model = models.RentalAgreement
        fields = (
            'id',
            'apartment',
            'start_date',
            'end_date',
            'tenant',
        )


