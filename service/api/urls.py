from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'apartments', views.ApartmentViewSet, 'apartments')
router.register(r'buildings', views.BuildingViewSet, 'buildings')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls)
] + router.urls
