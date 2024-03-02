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


def find_venues(payload):
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",  # trying this
    ]
    url = f"https://www.jambase.com/jb-api/v1/artists/id/jambase:3754557?expandPastEvents=true&apikey={payload}"
    response = requests.get(
        url, headers={"User-Agent": random.choice(user_agents_list)}
    )
    content = response.json()
    with open("./history.json", "w") as json_file:
        json.dump(content, json_file)


if __name__ == "__main__":
    payload = get_key()
    find_venues(payload)
