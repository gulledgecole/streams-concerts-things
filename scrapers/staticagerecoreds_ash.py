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

        div_elements = soup.find_all("div", class_="h-stack gap-4")
        data = {}
        iteration_counter = 1
        for div_element in div_elements:
            bands = div_element.find('h2', class_="text-md md:text-2xl flex-2").text.split(' / ')
            date = div_element.find('span', class_ = "").text
            date = helpers.date_handler(date)
            event_json = {
                "Venue": "Static Age Records",
                "Street": "110 N Lexington Ave",
                "City": "Ashville",
                "State": "North Carolina",
                "Long": "-82.553800",
                "Lat": "35.598580",
                "Capacity": "65",
                "Date": date,
                "Bands": bands,
            }
            data[iteration_counter] = event_json
            iteration_counter += 1
        return data
    else:
        print(f"{url} is not accessible")


data = scrape("https://www.staticagenc.com/events")
helpers.write_dict_to_json(data)

