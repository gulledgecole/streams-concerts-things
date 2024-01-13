from imports import *


def scrape(url):
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    ]
    data = requests.get(url, headers={"User-Agent": random.choice(user_agents_list)})
    if data.status_code == 200:
        html_content = data.text
        soup = BeautifulSoup(html_content, "html.parser")
        div_elements = soup.find_all(
            "div", class_="EventParts__EventBlock-sc-db999af1-9 gZUtAO"
        )
        data = {}
        iteration_counter = 1
        for div_element in div_elements:
            bands = div_element.find(
                "a", class_="EventParts__EventName-sc-db999af1-0 iOiUbH"
            ).text.split("/")
            ## "The Problem w/ kids today is literally the name of the band. Fucks everything up with all my logic, leaaving it."
            ## ['The Problem w', 'kids today', 'Vvebs', 'Wifey', 'The Problem w', 'Kids Today']
            bandz = [item.strip() for item in bands if item.strip()]
            date = div_element.find(
                "span", class_="EventParts__EventDate-sc-db999af1-1 hniCVa"
            ).text.strip()
            date = helpers.date_handler(date)
            event_json = {
                "Venue": "Gold Sounds",
                "Street": "44 Wilson Ave",
                "City": "Brookyln",
                "State": "New York",
                "Capacity": "150",
                "Date": date,
                "Bands": bands,
            }
            data[iteration_counter] = event_json
            iteration_counter += 1
        return data


data = scrape("https://dice.fm/venue/gold-sounds-y3qr")
helpers.write_dict_to_json(data)
