from imports import *

# Rocko Lounge, 117 Whitaker St, Savannah, GA 31401, USA


def scrape_elrocko_sav(url):
    data = requests.get(url)
    if data.status_code == 200:
        html_content = data.text
        iteration_counter = 1
        data = {}
        soup = BeautifulSoup(html_content, "html.parser")
        div_elements = soup.find_all("div", class_="Rz7J9y")
        for div_element in div_elements:
            bands = div_element.find("a", class_="DjQEyU")
            print(type(bands))


scrape_elrocko_sav("https://www.elrockolounge.com/")
