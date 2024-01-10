from imports import *


def scrape_greyeagleash(url):
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    ]
    data = requests.get(url, headers={"User-Agent": random.choice(user_agents_list)})
    print(data)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, "html.parser")
        print(soup)
        div_elements = soup.find_all("div", class_="col-12")
        print(div_elements)
        for div_element in div_elements:
            print(div_element.text.strip())


scrape_greyeagleash("https://www.thegreyeagle.com/calendar")
