from django.http import JsonResponse
from .models import Gov
from parliament.models import MemberOfParliament
from .serializers import GovSerializer, MpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class CustomUserThrottle(UserRateThrottle):
    """
    """
    rate = '10/day'


class CustomAnonThrottle(AnonRateThrottle):
    """
    """
    rate = '5/day'


@api_view(['GET', 'POST'])
def gov_list(request, format=None):
    """
    Gets elective offices
    """
    if request.method == 'GET':
        gov = Gov.objects.all()
        serializer = GovSerializer(gov, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GovSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def mps_list(request, format=None):
    """
    Gets all the mps
    """
    if request.method == 'GET':
        mps = MemberOfParliament.objects.all()
        serializer = MpSerializer(mps, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def mps_detail(request, id, format=None):
    """
    Gets, updates and deletes an mp
    """
    try:
        mp = MemberOfParliament.objects.get(pk=id)
    except MemberOfParliament.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MpSerializer(mp)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MpSerializer(mp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


gov_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
mps_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
mps_detail.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
