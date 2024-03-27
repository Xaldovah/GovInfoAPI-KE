import asyncio
import time
import requests
import re
from django.http import JsonResponse
from .models import Gov
from parliament.models import MemberOfParliament
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA
from .serializers import MpSerializer, SenatorSerializer, GovernorSerializer, McaSerializer
from .mp_utils import extract_page_data
from .senate_utils import extract_senate_data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
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


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@api_view(['GET', 'POST'])
def gov_list(request, format=None):
    """
    Gets elective offices
    """
    if request.method == 'GET':
        extract_page_data(driver)
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
        if mps.exists():
            serializer = MpSerializer(mps, many=True)
            return Response(serializer.data)

        driver.get('http://www.parliament.go.ke/the-national-assembly/mps')
        driver.maximize_window()

        # Extract data from the current page
        page_data = extract_page_data(driver)

        valid_data = [
                mp_data for mp_data in page_data if mp_data.get(
                    'constituency') and not mp_data[
                        'constituency'].strip().isdigit()]

        # Save data to the SQLite database
        for mp_data in valid_data:
            existing_mp = MemberOfParliament.objects.filter(
                    name=mp_data['name'],
                    constituency=mp_data['constituency'],
                    county=mp_data['county'],
                    party=mp_data['party']
            ).first()
            if not existing_mp:
                mp_object = MemberOfParliament(**mp_data)
                mp_object.save()

        driver.quit()

        mps = MemberOfParliament.objects.all()
        serializer = MpSerializer(mps, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        existing_mps = MemberOfParliament.objects.all()

        for mp_data in data:
            existing_mp = existing_mps.filter(
                    name=mp_data['name'],
                    constituency=mp_data['constituency'],
                    county=mp_data['county'],
                    party=mp_data['party']
            ).first()
            if existing_mp:
                continue
            serializer = MpSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                        serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def search_mp_by_constituency(request, constituency, format=None):
    """
    Get MP by constituency
    """
    if request.method == 'GET':
        constituency = constituency.lower()
        try:
            mp = MemberOfParliament.objects.get(constituency__iexact=constituency)
            serializer = MpSerializer(mp)
            return Response(serializer.data)
        except MemberOfParliament.DoesNotExist:
            return Response({"message": "MP not found for the given constituency"}, status=404)


@api_view(['GET', 'POST'])
def senators_list(request, format=None):
    """
    Gets all the senators
    """
    if request.method == 'GET':
        senators = Senators.objects.all()
        if senators.exists():
            serializer = SenatorSerializer(senators, many=True)
            return Response(serializer.data)

        driver.get('http://www.parliament.go.ke/the-senate/senators')
        driver.maximize_window()

        # Extract data from the current page
        page_data = extract_senate_data(driver)

        valid_data = [
                senator_data for senator_data in page_data if senator_data.get(
                    'county') and not senator_data[
                        'county'].strip().isdigit()]

        # Save data to the SQLite database
        for senator_data in valid_data:
            existing_senator = Senators.objects.filter(
                    name=senator_data['name'],
                    county=senator_data['county'],
                    party=senator_data['party']
            ).first()

            if not existing_senator:
                senator_object = Senators(**senator_data)
                senator_object.save()

        driver.quit()

        senators = Senators.objects.all()
        serializer = SenatorSerializer(senators, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def search_senator_by_county(request, county, format=None):
    """
    Get senator by county
    """
    if request.method == 'GET':
        county = county.lower()  # Convert to lowercase
        try:
            senator = Senators.objects.get(county__iexact=county)
            serializer = SenatorSerializer(senator)
            return Response(serializer.data)
        except Senators.DoesNotExist:
            return Response({"message": "Senator not found for the given county"}, status=404)


@api_view(['GET', 'POST'])
def governors_list(request, format=None):
    """
    Gets all the governors
    """
    if request.method == 'GET':
        governors = Governors.objects.all()
        if governors.exists():
            serializer = GovernorSerializer(governors, many=True)
            return Response(serializer.data)

        url = 'https://www.cog.go.ke/the-council/governors'
        response = requests.get(url)

        if response.status_code != 200:
            return Response(
                    {'error': 'Failed to fetch data from the website.'},
                    status=response.status_code)

        soup = BeautifulSoup(response.content, 'html.parser')

        data = []
        table = soup.find('table')
        table_body = table.find('tbody')

        governor_rows = table_body.find_all('tr')
        county_names = []
        county_prefixes = []

        for row in governor_rows:
            for cell in row.find_all('td', style='text-align: center;'):
                county_link = cell.find('a')
                if county_link:
                    county_name = county_link.text.strip()
                    county_prefix = county_name.split('.')[0].strip()
                    county_names.append(county_name)
                    county_prefixes.append(county_prefix)

        governors_data_rows = [row.find_all('td') for row in governor_rows]
        governor_data = []

        for county_name, county_prefix, data_row in zip(county_names, county_prefixes, governors_data_rows):
            for cell in data_row:
                governor_name = cell.text.strip()
                if governor_name and governor_name != county_name:
                    governor_data.append({
                        'name': governor_name,
                        'county': county_name
                    })

        # Save data to the SQLite database
        for governor_data_entry in governor_data:
                governor_object = Governors(**governor_data_entry)
                governor_object.save()

        governors = Governors.objects.all()
        serializer = GovernorSerializer(governors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def search_governor_by_county(request, county, format=None):
    """
    Get governor by county
    """
    if request.method == 'GET':
        county = ''.join(filter(str.isalpha, county)).lower()
        try:
            governor = Governors.objects.get(county__iexact=county)
            serializer = GovernorSerializer(governor)
            return Response(serializer.data)
        except Governors.DoesNotExist:
            return Response({"message": "Governor not found for the given county"}, status=404)


@api_view(['GET', 'POST'])
def mcas_list(request, format=None):
    """
    Gets all the members of the county assembly (MCAs)
    """
    if request.method == 'GET':
        mcas = MCA.objects.all()
        if mcas.exists():
            serializer = McaSerializer(mcas, many=True)
            return Response(serializer.data)

        url = requests.get('https://www.nyongesasande.com/mcas-in-kenya-per-county-2022-to-2027/')
        soup = BeautifulSoup(url.content, 'html.parser')

        mca_tags = soup.find_all('p')[4:]

        mca_names = [p.get_text(strip=True) for p in mca_tags]

        mca_text = ''.join(mca_names)

        mca_text_separated = re.sub(r'(\d+\.)', r'\n\1', mca_text)

        filtered_mcas = []
        for line in mca_text_separated.split('\n'):
            if not line.startswith('Check out other tags:') and not line.startswith('©Nyongesa Sande'):

                # Remove text from "Check" to the end of the line
                line = line.split('Check')[0].strip()
                filtered_mcas.append(line)

        # Process each filtered MCA entry and save to the database
        for entry in filtered_mcas:
            if ' – ' in entry and '(' in entry and ')' in entry:
                try:
                    mca_name = entry.split(' – ')[1].split(' (')[0].strip()
                    ward = entry.split('.')[1].split(' – ')[0].strip()
                    party = entry.split('(')[1].split(')')[0].strip()

                    mca = MCA(name=mca_name, ward=ward, party=party)
                    mca.save()
                except IndexError:
                    print(f"Error processing entry: {entry}")

        # Retrieve all MCAs from the database and return the response
        mcas = MCA.objects.all()
        serializer = McaSerializer(mcas, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def search_mca_by_ward(request, ward, format=None):
    """
    Get MCA by ward
    """
    if request.method == 'GET':
        ward = ward.lower()
        try:
            mca = MCA.objects.get(ward__iexact=ward)
            serializer = McaSerializer(mca)
            return Response(serializer.data)
        except MCA.DoesNotExist:
            return Response({"message": "MCA not found for the given ward"}, status=404)


gov_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
mps_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
search_mp_by_constituency.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
senators_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
search_senator_by_county.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
governors_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
search_governor_by_county.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
mcas_list.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
search_mca_by_ward.throttle_classes = [CustomUserThrottle, CustomAnonThrottle]
