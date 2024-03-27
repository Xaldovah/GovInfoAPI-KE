from rest_framework import serializers
from .models import Gov
from parliament.models import MemberOfParliament 
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA


class GovSerializer(serializers.ModelSerializer):
    """
    class to serialize the position data to json 
    """

    class Meta:
        """
        serializer
        """
        model = Gov
        fields = ['id', 'office', 'salary']      


class MpSerializer(serializers.ModelSerializer): 
    """
    class to serialize mps data to json
    """

    class Meta:
        """
        serializer
        """
        model = MemberOfParliament
        fields = ['id', 'name', 'constituency']


class SenatorSerializer(serializers.ModelSerializer):
    """
    class to serialize senators data to json
    """

    class Meta:
        """
        serializer
        """
        model = Senators
        fields = ['id', 'name', 'county']


class GovernorSerializer(serializers.ModelSerializer):
    """
    class to serialize governors data to json
    """

    class Meta:
        """
        serializer
        """
        model = Governors
        fields = ['id', 'name', 'county']


class McaSerializer(serializers.ModelSerializer):
    """
    class to serialize mcas data to json
    """

    class Meta:
        """
        serializer
        """
        model = MCA
        fields = ['id', 'name', 'ward']
