from django.test import TestCase
from .models import Governors

class GovernorsModelTestCase(TestCase):
    """Class model to test governor app"""
    def setUp(self):
        self.governor1 = Governors.objects.create(name="John Doe", county="County A", party="Party A")
        self.governor2 = Governors.objects.create(name="Jane Smith", county="County B", party="Party B")

    def test_governor_creation(self):
        """Test Governors model creation"""
        self.assertEqual(self.governor1.name, "John Doe")
        self.assertEqual(self.governor1.county, "County A")
        self.assertEqual(self.governor1.party, "Party A")
        self.assertEqual(self.governor2.name, "Jane Smith")
        self.assertEqual(self.governor2.county, "County B")
        self.assertEqual(self.governor2.party, "Party B")

    def test_governor_str_representation(self):
        """Test Governors model string representation"""
        self.assertEqual(str(self.governor1), "John Doe County A")
        self.assertEqual(str(self.governor2), "Jane Smith County B")


class GovernorsEdgeCasesTestCase(TestCase):
    def test_empty_name(self):
        """Test Governors model with empty name"""
        governor = Governors.objects.create(name="", county="County A", party="Party A")
        self.assertEqual(str(governor), " County A")  # Expecting only the county since name is empty

    def test_empty_county(self):
        """Test Governors model with empty county"""
        governor = Governors.objects.create(name="John Doe", county="", party="Party A")
        self.assertEqual(str(governor), "John Doe ")  # Expecting only the name since county is empty

    def test_empty_party(self):
        """Test Governors model with empty party"""
        governor = Governors.objects.create(name="John Doe", county="County A", party="")
        self.assertEqual(str(governor), "John Doe County A")  # Expecting name and county only since party is empty
