from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import MemberOfParliament

class MemberOfParliamentModelTestCase(TestCase):
    """
    Test case class for the MemberOfParliament model.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.mp1 = MemberOfParliament.objects.create(name="John Doe", constituency="Constituency A", county="County X", party="Party A")
        self.mp2 = MemberOfParliament.objects.create(name="Jane Smith", constituency="Constituency B", county="County Y", party="Party B")

    def test_empty_string_values(self):
        """
        Test for empty string values.
        """
        with self.assertRaises(ValidationError):
            MemberOfParliament.objects.create(name="", constituency="", county="", party="")

    def test_maximum_length_fields(self):
        """
        Test for maximum length of fields.
        """
        with self.assertRaises(ValidationError):
            MemberOfParliament.objects.create(name="X" * 101, constituency="Y" * 101, county="Z" * 101, party="W" * 101)

    def test_special_characters(self):
        """
        Test for special characters.
        """
        mp = MemberOfParliament.objects.create(name="Special!Name", constituency="Constituency$", county="County@", party="@Party")
        self.assertEqual(mp.name, "Special!Name")
        self.assertEqual(mp.constituency, "Constituency$")
        self.assertEqual(mp.county, "County@")
        self.assertEqual(mp.party, "@Party")

    def test_unique_constraints(self):
        """
        Test for unique constraints.
        """
        with self.assertRaises(ValidationError):
            MemberOfParliament.objects.create(name="John Doe", constituency="Constituency A", county="County X", party="Party A")

    def test_null_values(self):
        """
        Test for null values.
        """
        with self.assertRaises(ValidationError):
            MemberOfParliament.objects.create(name=None, constituency=None, county=None, party=None)
