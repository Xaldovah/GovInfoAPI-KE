import unittest
from django.urls import reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Gov
from parliament.models import MemberOfParliament
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA
from .serializers import (
    GovSerializer,
    MpSerializer,
    SenatorSerializer,
    GovernorSerializer,
    McaSerializer,
)

class TestGovViews(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('mps/', views.mps_list),
        path('mps/<str:constituency>/', views.search_mp_by_constituency),
        path('senators/', views.senators_list),
        path('senators/<str:county>/', views.search_senator_by_county),
        path('governors/', views.governors_list),
        path('governors/<str:county>/', views.search_governor_by_county),
        path('mcas/', views.mcas_list),
        path('mcas/<str:ward>/', views.search_mca_by_ward)
    ]

    def test_gov_list_get(self):
        """
        Test GET request for gov_list endpoint
        """
        url = reverse('gov_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gov_list_post(self):
        """
        Test POST request for gov_list endpoint
        """
        url = reverse('gov_list')
        data = {'office': 'example_office', 'salary': 'example_salary'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)


    def test_search_mp_by_constituency(self):
        """
        Test GET request for search_mp_by_constituency endpoint
        """
        url = reverse('search_mp_by_constituency', args=['example_constituency'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_mps_list_get(self):
        """
        Test GET request for mps_list endpoint
        """
        url = reverse('mps_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_mp_by_constituency(self):
        """
        Test GET request for search_mp_by_constituency endpoint
        """
        url = reverse('search_mp_by_constituency', args=['example_constituency'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_senators_list_get(self):
        """
        Test GET request for senators_list endpoint
        """
        url = reverse('senators_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_senator_by_county(self):
        """
        Test GET request for search_senator_by_county endpoint
        """
        url = reverse('search_senator_by_county', args=['example_county'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_governors_list_get(self):
        """
        Test GET request for governors_list endpoint
        """
        url = reverse('governors_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_governor_by_county(self):
        """
        Test GET request for search_governor_by_county endpoint
        """
        url = reverse('search_governor_by_county', args=['example_county'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_mcas_list_get(self):
        """
        Test GET request for mcas_list endpoint
        """
        url = reverse('mcas_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_mca_by_ward(self):
        """
        Test GET request for search_mca_by_ward endpoint
        """
        url = reverse('search_mca_by_ward', args=['example_ward'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

