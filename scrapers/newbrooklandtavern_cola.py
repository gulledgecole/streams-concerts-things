from imports import *


def scrape_newbrooklandtav(url):
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, "html.parser")
        div_elements = soup.find_all("div", class_="f_PoHs")
        for div_element in div_elements:
            bands = div_element.find("a", class_="DjQEyU").text.strip()
            bands = [
                bands.split("*")[0].strip().split("-")[0].strip()
            ]  # for some reason, this website adds a bunch of stuff after the bandname with * and -.
            bands = [item.strip() for item in bands[0].split(" w/")]
            bands = [
                item.strip() for item in bands[0].split(",")
            ]  # this website seperates bands by "," in title.
            date = div_element.find("div", class_="v2vbgt").text.strip()
            date = helpers.date_handler(date)
            event_json = {
                "Venue": "The New Brookland Tavern",
                "Street": "122 State St",  ## IT APPEARS THEY ARE MOVING LOCATIONS FYI
                "City": "West Columbia",
                "State": "South Carolina",
                "Long": "-81.056210",
                "Lat": "33.993820",
                "Capacity": "xxx",
                "Date": date,
                "Bands": bands,
            }
            data[iteration_counter] = event_json
            iteration_counter += 1
            ## NEED TO ADD ADD TO JSON AFTER NEW YEAR.

        return data


data = scrape_newbrooklandtav("https://www.newbrooklandtavern.com/")
helpers.write_dict_to_json(data)
