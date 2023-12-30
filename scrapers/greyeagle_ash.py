from bs4 import BeautifulSoup
from dateutil import parser
import date_shift
import json
import requests
import re

def scrape_greyeagleash(url):
    headers = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    data = requests.get(url)
    print(data)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup)
        div_elements = soup.find_all('div', class_="col-12")
        print(div_elements)
        for div_element in div_elements:
            print(div_element.text.strip())


scrape_greyeagleash("https://www.thegreyeagle.com/calendar")