from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from . import models


TEST_PASSWORD = '1234'


def get_logged_in_client(user):
    client = APIClient()
    user.is_form_authenticated = True
    client.login(username=user.username, password=TEST_PASSWORD)
    return client


# TODO: Unit tests seem to use the same database
class ApartmentViewSetTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='Test')
        self.user.set_password(TEST_PASSWORD)
        self.user.save()
        self.client = get_logged_in_client(self.user)

        building = models.Building.objects.get(
            street="Skyttegatan", street_number='7B', city="Eskilstuna"
        )
        self.number_of_apartments = models.Apartment.objects.count()
        payload = {
            "id": '42',
            "rent": 7938,
            "rooms": 2,
            "floor": 0,
            "area": 50,
        }
        self.apartment = models.Apartment.objects.create(building=building, **payload)

        self.list_url = reverse('apartments-list')
        self.detail_url = reverse('apartments-detail', kwargs=dict(pk=self.apartment.id))

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.number_of_apartments + 1)

    def test_list_unauthenticated(self):
        response = APIClient().get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.apartment.id)

    def test_retrieve_unauthenticated(self):
        response = APIClient().get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        data = {
            "id": '43',
            "building": self.apartment.building.id,
            "rent": 7938,
            "rooms": 2,
            "floor": 0,
            "area": 50,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], '43')
        self.assertEqual(response.data['building'], self.apartment.building.id)

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BuildingViewSetTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='Test')
        self.user.set_password(TEST_PASSWORD)
        self.user.save()
        self.client = get_logged_in_client(self.user)

        payload = {
            "street": "Skyttegatan",
            "street_number": "7C",
            "city": "Eskilstuna",
            "latitude": "59.3668802",
            "longitude": "16.4982711",
        }
        self.number_of_buildings = models.Building.objects.count()
        self.building = models.Building.objects.create(**payload)

        self.list_url = reverse('buildings-list')
        self.detail_url = reverse('buildings-detail', kwargs=dict(pk=self.building.id))

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.number_of_buildings + 1)

    def test_list_unauthenticated(self):
        response = APIClient().get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.building.id)

    def test_retrieve_unauthenticated(self):
        response = APIClient().get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        data = {
            "street": "Skyttegatan",
            "street_number": "7D",
            "city": "Eskilstuna",
            "latitude": "59.3668802",
            "longitude": "16.4982711",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['street_number'], '7D')

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class RentalAgreementViewSetTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='Test')
        self.user.set_password(TEST_PASSWORD)
        self.user.save()
        self.client = get_logged_in_client(self.user)

        # TODO: Fix when test db is isolated properly
        building = models.Building.objects.get(
            street="Skyttegatan", street_number='7B', city="Eskilstuna"
        )
        apartment_payload = {
            "id": '42',
            "rent": 7938,
            "rooms": 2,
            "floor": 0,
            "area": 50,
        }
        self.apartment = models.Apartment.objects.create(building=building, **apartment_payload)
        self.number_of_rental_agreements = models.RentalAgreement.objects.count()
        self.rental_agreement = models.RentalAgreement.objects.create(
            apartment=self.apartment, tenant=self.user, start_date=date(2022, 5, 4)
        )

        self.list_url = reverse('rental_agreements-list')
        self.detail_url = reverse('rental_agreements-detail', kwargs=dict(pk=self.rental_agreement.id))

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.number_of_rental_agreements + 1)

    def test_list_unauthenticated(self):
        response = APIClient().get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.rental_agreement.id)

    def test_retrieve_unauthenticated(self):
        response = APIClient().get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        data = {
            "apartment": self.apartment.id,
            "tenant": self.user.id,
            "start_date": date(2022, 1, 1),
            "end_date": date(2022, 12, 31),
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['tenant'], self.user.id)

    def test_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)