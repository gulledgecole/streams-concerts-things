from imports import *

# trying to scrape Jambase to see how it goes. 

# Mercury lounge seems to up to date with it.

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
        div_elements = soup.find_all('script', type='application/ld+json')
        for div_element in div_elements[8:9]:
            bands = []
            content = json.loads((div_element.text.strip()))
            for i in (content["performer"]):
                bands.append(i['name'])
            for j in (content["location"]): 
                print(j)
            print(bands)

        #print(div_elements)
        data = {}
        iteration_counter = 1

        # Iterate through each div element
        # for div_element in div_elements:
        #     print(div_element.text)


scrape("https://www.jambase.com/venue/mercury-lounge")
