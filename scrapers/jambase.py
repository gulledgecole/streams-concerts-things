from imports import *
from dateutil import parser
from datetime import datetime
import inspect
import os

from google.cloud import secretmanager


def get_key():
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/639888050178/secrets/jambase/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    return payload


def write_file(content, subfolder_name):
    today_date = datetime.now().strftime("%Y-%m-%d")
    # Get the current script's directory (assumes the script is in "scrapers")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the "concerts" folder at the same level
    concerts_folder = os.path.abspath(os.path.join(script_directory, "..", "concerts"))
    # Construct the path to the subfolder within the "concerts" folder
    subfolder_path = os.path.join(concerts_folder, subfolder_name)
    # Check if the subfolder exists
    if not os.path.exists(subfolder_path):
        # If not, create the subfolder
        os.makedirs(subfolder_path)
        print(f"Directory '{subfolder_name}' created successfully in 'concerts'.")
    file_path = os.path.join(subfolder_path, f"{subfolder_name}_{today_date}.json")
    with open(file_path, "w") as json_file:
        json.dump(content, json_file, indent=2)

    return


def find_venues(payload):
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  # trying this
    ]
    url = "https://www.jambase.com/jb-api/v1/venues"
    ## Apepars 212 is when it cuts off metro IDs.
    metro_ids = list(range(1, 211))
    for metro_id in metro_ids:
        print(metro_id)

        params = {
            "perPage": "1000",
            "geoMetroId": f"jambase:{metro_id}",
            "venueHasUpcomingEvents": "true",
            "apikey": payload,
        }

        response = requests.get(
            url, headers={"User-Agent": random.choice(user_agents_list)}, params=params
        )
        content = response.json()
        content = content["venues"]
        with open(f"../venues/jambase_{metro_id}.json", "w") as json_file:
            json.dump(content, json_file, indent=2)


def bandjam(venue_id, payload):
    data = []
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  # trying this
    ]
    params = {"expandUpcomingEvents": "true", "apikey": payload}
    url = f"https://www.jambase.com/jb-api/v1/venues/id/{venue_id}"
    response = requests.get(
        url, headers={"User-Agent": random.choice(user_agents_list)}, params=params
    )
    content = response.json()
    name = content["venue"]["name"]
    folder_name = name.replace(" ", "_")
    modification_date = content["venue"]["dateModified"]
    events = content["venue"]["events"]
    for event in events:
        performers = event.get("performer", [])
        offers = event.get("offers", [])
        for offer in offers:
            price = offer["priceSpecification"]
            seller = offer["seller"]

        event_json = {
            "venue": name,
            "venue_id": venue_id,
            "last_modified": modification_date,
            "price": price,
            "seller": seller,
            "bands": performers,
        }
        data.append(event_json)

    return data, folder_name


if __name__ == "__main__":
    count = 0
    payload = get_key()
    find_venues(payload)
    # with open("dump.json", "r") as file:
    #     dump = json.load(file)
    # # Iterate over the keys and process "id" values
    # for i in dump:
    #     count += 1
    #     print(count)
    #     venue_id = i.get("identifier")
    #     response, folder_name = bandjam(venue_id, payload)
    #     write_file(response, folder_name)
