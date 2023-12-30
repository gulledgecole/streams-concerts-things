from bs4 import BeautifulSoup
from dateutil import parser
import scraper
import json
import requests
import re


def scrape_windjammer_bit(url):
    div_elements, iteration_counter, data = scraper.scraper(url, "tY_uoLi0K4FrxkcoAV7k")
    print(div_elements)


scrape_windjammer_bit("https://www.bandsintown.com/v/10002896-windjammer/")
