# Events API To collect fan data and grow your audience

# Example of API calls using your artist name. (e.g. Justin Bieber):

# - artist profile info: https://rest.bandsintown.com/artists/Justin%20Bieber/?app_id=write_here_your_app-id
# ﻿ (returns the Bandsintown artist ID, the nb of followers, the photo, the nb of upcoming events, and a link to the artist profile on Bandsintown)

# - same call with the Bandsintown artist ID instead of the artist name: https://rest.bandsintown.com/artists/id_307871/?app_id=write_here_your_app-id

# - upcoming events: https://rest.bandsintown.com/artists/Justin%20Bieber/events?app_id=write_here_your_app-id

# - past events: https://rest.bandsintown.com/artists/Justin%20Bieber/events?app_id=write_here_your_app-id&date=past

# - all events: https://rest.bandsintown.com/artists/Justin%20Bieber/events?app_id=write_here_your_app-id&date=all

# - events on a date range (e.g. the year 2018): https://rest.bandsintown.com/artists/Justin%20Bieber/events?app_id=write_here_your_app-id&date=2013-01-01,2013-12-31

import requests
from google.cloud import secretmanager

def get_key(): 
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/639888050178/secrets/bands-in-town/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")
    
    return payload

def reach_bit(artist, payload):
    url =  f"https://rest.bandsintown.com/artists/The%20Thing/?app_id={payload}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        print(response.text)
        print(response.headers)
        print(response.status_code)
    else:
        print(f"Request failed with status code: {response.status_code}")


key = get_key()
reach_bit("foo", key)
