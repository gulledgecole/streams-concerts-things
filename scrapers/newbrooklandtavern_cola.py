from bs4 import BeautifulSoup
from dateutil import parser
import date_shift
import json
import requests
import re

def scrape_newbrooklandtav(url):
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, 'html.parser')
        div_elements = soup.find_all('div', class_="f_PoHs")
        for div_element in div_elements:
            print(div_element.text.strip())



scrape_newbrooklandtav("https://www.newbrooklandtavern.com/")