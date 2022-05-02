from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from .views import ApartmentViewSet


router = routers.SimpleRouter()
router.register(r'apartments', ApartmentViewSet, 'apartments')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls)
] + router.urls
