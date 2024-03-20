import os
import requests
import django
from models import MemberOfParliament
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gov.settings')
django.setup()

url = 'http://www.parliament.go.ke/the-national-assembly/mps'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    mp_elems = soup.find_all('tr', class_='mp')

    for mp in mp_elems:
        name = mp.find('td', class_='views-field views-field-field-name').text.strip()
        constituency = mp.find('td', class_='views-field views-field-field-constituency').text.strip()
        county = mp.find('td', class_='views-field views-field-field-county').text.strip()
        party = mp.find('td', class_='views-field views-field-field-party').text.strip()
        if constituency:
            mp_obj = MemberOfParliament.objects.create(
                    name=name,
                    constituency=constituency,
                    county=county,
                    party=party
            )
            print(f'Member of Parliament saved: {mp_obj.name}')
        else:
            print('Not saved')
else:
    print('Failed to retrieve data from the website')
