from rest_framework import serializers
from .models import Gov
from parliament.models import MemberOfParliament


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
