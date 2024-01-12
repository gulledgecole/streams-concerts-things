from imports import *


def scrape_pour(url):
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, "html.parser")
        tokens = soup.find_all()
        num_tokens = len(tokens)
        print(num_tokens)
        div_elements = soup.find_all(
            "div", class_="tribe-events-calendar-list__event-wrapper tribe-common-g-col"
        )
        for div_element in div_elements:
            bands = div_element.find(
                "a",
                class_="tribe-events-calendar-list__event-title-link tribe-common-anchor-thin",
            ).text.strip()
            date = div_element.find("time")["datetime"]
            date = helpers.date_handler(date)
            event_json = {
                "Venue": "The Charleston Pour House",
                "Street": "1977 Maybank Highway",
                "City": "Charleston",
                "State": "South Carolina",
                "Long": "-79.986960",
                "Lat": "32.762050",
                "Capacity": "450",
                "Date": date,
                "Bands": [bands],
            }
            data[iteration_counter] = event_json
            iteration_counter += 1

        return data


event = scrape_pour("https://charlestonpourhouse.com/shows/")
date_shift.write_dict_to_json(event)
