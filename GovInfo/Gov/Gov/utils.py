import sys
sys.path.append('..')
import requests
from bs4 import BeautifulSoup
from parliament.models import MemberOfParliament
import time

def find_mps():
    url = 'http://www.parliament.go.ke/the-national-assembly/mps'
    response = requests.get(url).text

    soup = BeautifulSoup(response, 'lxml')
    mp_elems = soup.find_all('tr', class_='mp')

    for index, mp in enumerate(mp_elems):
        name = mp.find('td', class_='views-field views-field-field-name').text.strip()
        constituency = mp.find('td', class_='views-field views-field-field-constituency').text.strip()
        county = mp.find('td', class_='views-field views-field-field-county').text.strip()
        party = mp.find('td', class_='views-field views-field-field-party').text.strip()
        
        if constituency:
            mp_object = MemberOfParliament(name=name, constituency=constituency, county=county, party=party)
            mp_object.save()


if __name__ == '__main__':
    while True:
        find_mps()
        time.sleep(24 * 60 * 60)
