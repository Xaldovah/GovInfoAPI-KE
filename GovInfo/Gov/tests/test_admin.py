from django.test import TestCase
from django.contrib import admin
from .models import Gov
from parliament.models import MemberOfParliament
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA

class AdminSiteTestCase(TestCase):
    def test_gov_model_registered(self):
        """
        Test that the Gov model is registered in the admin site.
        """
        self.assertIn(Gov, admin.site._registry)

    def test_member_of_parliament_model_registered(self):
        """
        Test that the MemberOfParliament model is registered in the admin site.
        """
        self.assertIn(MemberOfParliament, admin.site._registry)

    def test_senators_model_registered(self):
        """
        Test that the Senators model is registered in the admin site.
        """
        self.assertIn(Senators, admin.site._registry)

    def test_governors_model_registered(self):
        """
        Test that the Governors model is registered in the admin site.
        """
        self.assertIn(Governors, admin.site._registry)

    def test_mca_model_registered(self):
        """
        Test that the MCA model is registered in the admin site.
        """
        self.assertIn(MCA, admin.site._registry)
