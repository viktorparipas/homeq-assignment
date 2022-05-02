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
