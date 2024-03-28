from django.test import TestCase
from .models import MCA

class MCAModelTestCase(TestCase):
    """Class model test for county app"""
    def setUp(self):
        self.mca1 = MCA.objects.create(name="John Doe", ward="Ward A", party="Party A")
        self.mca2 = MCA.objects.create(name="Jane Smith", ward="Ward B", party="Party B")

    def test_mca_creation(self):
        """Test MCA model creation"""
        self.assertEqual(self.mca1.name, "John Doe")
        self.assertEqual(self.mca1.ward, "Ward A")
        self.assertEqual(self.mca1.party, "Party A")
        self.assertEqual(self.mca2.name, "Jane Smith")
        self.assertEqual(self.mca2.ward, "Ward B")
        self.assertEqual(self.mca2.party, "Party B")

    def test_mca_str_representation(self):
        """Test MCA model string representation"""
        self.assertEqual(str(self.mca1), "John Doe Ward A")
        self.assertEqual(str(self.mca2), "Jane Smith Ward B")


class MCAEdgeCasesTestCase(TestCase):
    def test_empty_name(self):
        """Test MCA model with empty name"""
        mca = MCA.objects.create(name="", ward="Ward A", party="Party A")
        self.assertEqual(str(mca), " Ward A")  # Expecting only the ward since name is empty

    def test_empty_ward(self):
        """Test MCA model with empty ward"""
        mca = MCA.objects.create(name="John Doe", ward="", party="Party A")
        self.assertEqual(str(mca), "John Doe ")  # Expecting only the name since ward is empty

    def test_empty_party(self):
        """Test MCA model with empty party"""
        mca = MCA.objects.create(name="John Doe", ward="Ward A", party="")
        self.assertEqual(str(mca), "John Doe Ward A")  # Expecting name and ward only since party is empty
