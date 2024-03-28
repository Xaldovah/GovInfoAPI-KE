import unittest
from rest_framework.exceptions import ValidationError
from Gov.serializers import GovSerializer, MpSerializer, SenatorSerializer, GovernorSerializer, McaSerializer
from .models import Gov
from parliament.models import MemberOfParliament
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA

class TestSerializers(unittest.TestCase):
    def test_gov_serializer(self):
        data = {'office': 'President', 'salary': 1000000}
        serializer = GovSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_mp_serializer(self):
        data = {'name': 'John Doe', 'constituency': 'Example Constituency'}
        serializer = MpSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_senator_serializer(self):
        data = {'name': 'Jane Doe', 'county': 'Example County'}
        serializer = SenatorSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_governor_serializer(self):
        data = {'name': 'Alice Smith', 'county': 'Example County'}
        serializer = GovernorSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_mca_serializer(self):
        data = {'name': 'Bob Johnson', 'ward': 'Example Ward'}
        serializer = McaSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        invalid_data = {'office': '', 'salary': 'not_a_number'}
        serializer = GovSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.validate(invalid_data)

if __name__ == '__main__':
    unittest.main()
