from bs4 import BeautifulSoup
from dateutil import parser
import json
import requests
import re


def scrape_pour(url): 
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        soup = BeautifulSoup(html_content, 'html.parser')

