from dateutil import parser
from datetime import datetime
import requests
import json
import inspect
import os
import re

## Need to add exception when year is not provided.


def date_checker(dates):
    """Checks the date format, this will be updated as more websites do random things with their dates.
    Thank god for GPT, I hate regex.
    Return the value to be passed into the date handler, which formats the dates across all venues.
    Super weird ones, such as:SUNDAYS, 6 PM – 2 AM aren't worth the time."""

    date_patterns = [
        r"\d{1,2}/\d{1,2}/\d{2,4}",  # Example: 12/31/2022
        r"\d{1,2}-\d{1,2}-\d{2,4}",  # Example: 12-31-2022
        r"\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{2,4}",  # Example: 12 Jan 2022
        r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{2,4}",  # Example: 12 January 2022
        r"(?:SUNDAY|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY),\s+(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+\d{1,2}",  # Example: WEDNESDAY, JANUARY 31
        r"(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat),\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}",  # Example: Thu, Feb 08
        r"(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat),\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{2,4}",  # Example: Fri, Jan 12, 2024
        r"(Sun|Mon|Tue|Wed|Thu|Fri|Sat|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday) (January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}",
    ]

    return any(re.search(pattern, dates, re.I) for pattern in date_patterns)


def date_handler(dates):
    """Takes in a date, spits out a date in the format I like.
    Wed, Feb 08, 2024 for example.
    If a year is not provided, it assumes the current year, which I do not hate.
    If its a dumb output, as mentioned in above function, datechecker, it just reutnrs xxx.
    """
    if date_checker(dates):
        datez = parser.parse(dates)
        datez = datez.strftime("%a, %b %d, %Y")
    else:
        datez = dates

    return datez


def write_dict_to_json(dictionary):
    """
    Write a dictionary to a JSON file.

    Parameters:
    - dictionary (dict): The dictionary to be written to the JSON file.
    - file_path (str): The path to the JSON file.

    Returns:
    - None
    """
    # Ensure that the "./concerts/" folder exists
    today_date = datetime.now().strftime("%Y-%m-%d")
    frame = inspect.stack()[1]
    filename = os.path.splitext(os.path.basename(frame[1]))[0]
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, "..", "concerts", filename)
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, f"{filename}_{today_date}.json")
    with open(file_path, "w") as json_file:
        json.dump(dictionary, json_file, indent=2)

    return


def scraper(url, find_all):
    try:
        data = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        session = requests.Session()
        response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})
        # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        if data.status_code == 200:
            html_content = data.text
            soup = BeautifulSoup(html_content, "html.parser")
            div_elements = soup.find_all("div", class_=find_all)
            data = {}
            iteration_counter = 1

            return div_elements, iteration_counter, data
    except requests.exceptions.RequestException as e:
        print(f"request is failing, as a result of {e}")

    return
