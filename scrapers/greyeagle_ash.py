from imports import *

## GREY EAGLE IS PISSING ME OFF, MOVING TO NEXT ONE.


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
        prettified_html = soup.prettify()

        # Specify the file name to write the HTML content
        # output_file = "output.html"

        # # Write the prettified HTML string to the file
        # with open(output_file, "w", encoding="utf-8") as file:
        #     file.write(prettified_html)
        #div_elements = soup.find_all("div", class_="col-12 px-0 eventTitleDiv")
        div_elements = soup.find_all("div", class_="row g-0")
        for div_element in div_elements[:8]:
            try: 
                #date = div_element.find("div", class_="mb-0 eventMonth singleEventDate text-uppercase", id_="eventDate")
                band = div_element.find('h2', class_ = "mb-1 font1by25 font1By5remMD marginBottom3PX font1By75RemSM font1By5RemXS")
                if band:
                    band = (band.text.strip())
                    #date = (date.text.strip())
                    #print(date)
                    print(band)
                else: 
                    continue
            except Exception as e: 
                print(f"An error occurred: {e}")

            continue

scrape_greyeagleash("https://www.thegreyeagle.com/calendar")
