from bs4 import BeautifulSoup
from dateutil import parser
import requests
import re


def date_handler(date):
    try: 
        date = parser.parse(date)
        date = date.strftime("%a, %b %d, %Y") 
    except Exception as e: 
        print(f"there was an error with {date}, see error {e}")

    return date

def scrape_royal(): 
    url = 'https://www.theroyalamerican.com/schedule/'

    data = requests.get(url)

    #print(data.text)
    if data.status_code == 200:
    # Get the HTML content from the response
        html_content = data.text
        soup = BeautifulSoup(html_content, 'html.parser')
        div_elements = soup.find_all('div', class_='eventlist-column-info')
        if div_elements:
            for div_element in div_elements:
                title = div_element.find('h1', class_='eventlist-title').text.strip()
                date = div_element.find('time', class_="event-date").text.strip()
                date = date_handler(date)
                input_string = div_element.find('div', class_="eventlist-description").find('p')
                cleaned_band_list1 = [a.get_text(strip=True)[2:] for a in input_string.find_all('a') if a.get_text(strip=True)]
                cleaned_band_list = [band for band in cleaned_band_list1 if band]
                event_json = {
                    "Title": title,
                    "Date": date,
                    "Bands" : cleaned_band_list
                }
        else:
            print("No div elements with the specified class found.")
if __name__ == '__main__':
    scrape_royal()