from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers
from .framework import ViewMixIn


class ApartmentViewSet(ViewMixIn, ReadOnlyModelViewSet):
    serializer_class = serializers.ApartmentSerializer

    def get_queryset(self):
        return models.Apartment.objects.all()
