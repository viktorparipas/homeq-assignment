from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers
from .framework import CreateModelMixInWithObjectPermissionCheck, ViewMixIn


class ApartmentViewSet(
    CreateModelMixInWithObjectPermissionCheck,
    mixins.DestroyModelMixin,
    ViewMixIn,
    ReadOnlyModelViewSet
):
    serializer_class = serializers.ApartmentSerializer

    def get_queryset(self):
        return models.Apartment.objects.all()


class BuildingViewSet(
    CreateModelMixInWithObjectPermissionCheck,
    ViewMixIn,
    ReadOnlyModelViewSet
):
    serializer_class = serializers.BuildingSerializer

    def get_queryset(self):
        return models.Building.objects.all()


class RentalAgreementViewSet(
    CreateModelMixInWithObjectPermissionCheck,
    ViewMixIn,
    ReadOnlyModelViewSet
):
    serializer_class = serializers.RentalAgreementSerializer

    def get_queryset(self):
        return models.RentalAgreement.objects.all()
