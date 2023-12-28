from bs4 import BeautifulSoup
from dateutil import parser
import date_shift
import json
import requests
import re 

def scrape_musicfarm_chas(url): 
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        soup = BeautifulSoup(html_content, 'html.parser')
        div_elements = soup.find_all('div', class_='event-bottom')
        data = {}
        iteration_counter = 1
        if div_elements:
            for div_element in div_elements:
                bands = []
                band_headline = div_element.find('div', class_ = "event-title").text.strip()
                if "+" in band_headline:
                    band_headline = band_headline.replace('+', ',').replace(' ,', ',')
                bands.append(band_headline)
                band_support = div_element.find('div', class_ = "event-supporting-acts")
                if band_support:
                    bands.append(band_support.text.strip().replace('w/ ', ''))

scrape_musicfarm_chas("https://www.musicfarm.com/calendar/")