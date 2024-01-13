from imports import *

# really weird one, had to go to try to buy ticket to see all events.
# bad website


def scrape_windjammer(url):
    data = requests.get(url)
    if data.status_code == 200:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        html_content = data.text
        soup = BeautifulSoup(html_content, "html.parser")
        div_elements = soup.find_all("div", class_="col-md-6")
        data = {}
        iteration_counter = 1
        for div_element in div_elements:
            bands = []
            band = div_element.find("h4").text.strip()
            band = [
                re.sub(r" 21.*", "", band).replace("-", "").strip()
            ]  # removing everything after "21* and up!"
            bands = [item.strip() for item in band[0].split(" w/")]
            bands = [
                item.split(maxsplit=1)[1].strip()
                if item.split(maxsplit=1)[0] in days
                else item
                for item in bands
            ]  # hate this line. removing days of week.
            date = div_element.find("p").text.strip()
            date = re.sub(r"\b2024\b.*", "2024", date)
            date = helpers.date_handler(date)
            event_json = {
                "Venue": "The Windjammer",
                "Street": "1008 Ocean Blvd",
                "City": "Isle of Palms",
                "State": "South Carolina",
                "Long": "-79.790080",
                "Lat": "32.784520",
                "Capacity": "550",
                "Date": date,
                "Bands": bands,
            }
            data[iteration_counter] = event_json
            iteration_counter += 1
        return data


event = scrape_windjammer(
    "https://whollyticket.com/upcomingEvents/?id=67%20-%20ticketing"
)
helpers.write_dict_to_json(event)
