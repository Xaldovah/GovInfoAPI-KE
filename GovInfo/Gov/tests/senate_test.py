from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Senators

class SenatorsModelTestCase(TestCase):
    def setUp(self):
        self.senator1 = Senators.objects.create(name="John Doe", county="County A", party="Party A")
        self.senator2 = Senators.objects.create(name="Jane Smith", county="County B", party="Party B")

    def test_senator_creation(self):
        """Test Senators model creation"""
        self.assertEqual(self.senator1.name, "John Doe")
        self.assertEqual(self.senator1.county, "County A")
        self.assertEqual(self.senator1.party, "Party A")
        self.assertEqual(self.senator2.name, "Jane Smith")
        self.assertEqual(self.senator2.county, "County B")
        self.assertEqual(self.senator2.party, "Party B")

    def test_senator_str_representation(self):
        """Test Senators model string representation"""
        self.assertEqual(str(self.senator1), "John Doe County A")
        self.assertEqual(str(self.senator2), "Jane Smith County B")


class SenatorsModelTestCase(TestCase):
    def setUp(self):
        self.senator1 = Senators.objects.create(name="John Doe", county="County A", party="Party A")
        self.senator2 = Senators.objects.create(name="Jane Smith", county="County B", party="Party B")

    # Test for empty string values
    def test_empty_string_values(self):
        with self.assertRaises(ValidationError):
            Senators.objects.create(name="", county="County C", party="")

    # Test for maximum length of fields
    def test_maximum_length_fields(self):
        with self.assertRaises(ValidationError):
            Senators.objects.create(name="X" * 101, county="Y" * 101, party="Z" * 101)

    # Test for special characters
    def test_special_characters(self):
        senator = Senators.objects.create(name="Special!Name", county="County$", party="@Party")
        self.assertEqual(senator.name, "Special!Name")
        self.assertEqual(senator.county, "County$")
        self.assertEqual(senator.party, "@Party")

    # Test for unique constraints
    def test_unique_constraints(self):
        with self.assertRaises(ValidationError):
            Senators.objects.create(name="John Doe", county="County A", party="Party A")

    # Test for null values
    def test_null_values(self):
        with self.assertRaises(ValidationError):
            Senators.objects.create(name=None, county=None, party=None)
