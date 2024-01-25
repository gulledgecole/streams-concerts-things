import requests
import random

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
    print(venue_id)
    folder_name = name.replace(" ", "_")
    modification_date = content["venue"]["dateModified"]
    events = content["venue"]["events"]
    for event in events:
        performers = event.get("performer", [])
        offers = event.get("offers", [])
        if not offers:
            # Set default values if the "offers" list is empty
            price = {}
            seller = {}
        else:
            # Iterate over each offer in the "offers" list
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