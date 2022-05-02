from django.urls import path
from rest_framework import routers

from .views import ApartmentViewSet


router = routers.SimpleRouter()
router.register(r'apartments', ApartmentViewSet, 'apartments')

urlpatterns = router.urls
