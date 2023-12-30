from bs4 import BeautifulSoup
from dateutil import parser
import date_shift
import json
import requests
import re 

from urllib.request import Request, urlopen

req = Request(
    url='http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()

def scraper(url, find_all): 
    try: 
        data = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'} )
        session = requests.Session()
        response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        #req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        if data.status_code == 200:
            html_content = data.text
            soup = BeautifulSoup(html_content, 'html.parser')
            div_elements = soup.find_all('div', class_=find_all)
            data = {}
            iteration_counter = 1

            return div_elements, iteration_counter, data
    except requests.exceptions.RequestException as e:
        print(f'request is failing, as a result of {e}')
