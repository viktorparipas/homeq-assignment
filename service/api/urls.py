from django.urls import path

from .views import ApartmentsView


urlpatterns = [
    path("apartments/", ApartmentsView.as_view()),
]
