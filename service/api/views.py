from django.http import JsonResponse
from django.views import View
from .models import Apartment


class ApartmentsView(View):

    def get(self, request):
        apartments = Apartment.objects.all()
        serialized_data = [apartment.serialize() for apartment in apartments]
        return JsonResponse(serialized_data, safe=False)
