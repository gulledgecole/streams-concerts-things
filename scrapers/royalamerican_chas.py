from imports import *


def scrape_royal(url):
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        soup = BeautifulSoup(html_content, "html.parser")
        div_elements = soup.find_all("div", class_="eventlist-column-info")
        data = {}
        iteration_counter = 1
        tokens = soup.find_all()
        num_tokens = len(tokens)
        print(num_tokens)
        if div_elements:
            for div_element in div_elements:
                title = div_element.find("h1", class_="eventlist-title").text.strip()
                date = div_element.find("time", class_="event-date").text.strip()
                date = helpers.date_handler(date)
                input_string = div_element.find(
                    "div", class_="eventlist-description"
                ).find("p")
                cleaned_band_list1 = [
                    a.get_text(strip=True)[2:]
                    for a in input_string.find_all("a")
                    if a.get_text(strip=True)
                ]
                cleaned_band_list = [band for band in cleaned_band_list1 if band]
                event_json = {
                    "Venue": "The Royal American",
                    "Street": "970 Morrison Dr",
                    "City": "Charleston",
                    "State": "South Carolina",
                    "Long": "-79.942380",
                    "Lat": "32.807180",
                    "Capacity": "320",
                    "Date": date,
                    "Bands": cleaned_band_list,
                }
                data[iteration_counter] = event_json
                iteration_counter += 1
        else:
            print("No div elements with the specified class found.")

        return data


event = scrape_royal("https://www.theroyalamerican.com/schedule/")
helpers.write_dict_to_json(event)
