from dateutil import parser
from datetime import datetime
import json
import os

def date_handler(date):
    try: 
        date = parser.parse(date)
        date = date.strftime("%a, %b %d, %Y") 
    except Exception as e: 
        print(f"there was an error with {date}, see error {e}")

    return date

def write_dict_to_json(dictionary, filename):
    """
    Write a dictionary to a JSON file.

    Parameters:
    - dictionary (dict): The dictionary to be written to the JSON file.
    - file_path (str): The path to the JSON file.

    Returns:
    - None
    """
    # Ensure that the "./concerts/" folder exists
    today_date = datetime.now().strftime('%Y-%m-%d')
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, '..', 'concerts', filename)
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, f"{filename}_{today_date}.json")
    with open(file_path, 'w') as json_file:
        json.dump(dictionary, json_file, indent=2)