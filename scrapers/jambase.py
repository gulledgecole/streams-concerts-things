from imports import *

from google.cloud import secretmanager


def get_key():
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/639888050178/secrets/jambase/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    return payload

def bandjam(url, payload):
    data = []
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    ]
    params = {"expandUpcomingEvents": "true", "apikey": payload}
    response = requests.get(
        url, headers={"User-Agent": random.choice(user_agents_list)}, params=params
    )
    content = response.json()
    name = content["venue"]["name"]
    modification_date = content["venue"]["dateModified"]
    address = content["venue"]["address"]["streetAddress"]
    city = content["venue"]["address"]["addressLocality"]
    zip_code = content["venue"]["address"]["postalCode"]
    state = content["venue"]["address"]["addressRegion"]["name"]
    jameBaseCityId = content["venue"]["address"]["x-jamBaseCityId"]
    longitude = content["venue"]["geo"]["longitude"]
    latitude = content["venue"]["geo"]["latitude"]
    venue_url = content["venue"]["sameAs"][0]["url"]
    capacity = content["venue"]["maximumAttendeeCapacity"]
    events = content["venue"]["events"]
    for event in events:
        performers = event.get("performer", [])
        event_json = {
            "venue": name,
            "street": address,
            "venue_url": venue_url,
            "last_modified": modification_date,
            "city": city,
            "ctate": state,
            "zipcode": zip_code,
            "jame_base_city_id": jameBaseCityId,
            "long": longitude,
            "lat": latitude,
            "capacity": capacity,
            "bands": performers,
        }
        data.append(event_json)
    output_file_path = "output.json"
    with open(output_file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

    return response.json()

url = "https://www.jambase.com/jb-api/v1/venues/id/jambase:6231804"
payload = get_key()
response = bandjam(url, payload)
