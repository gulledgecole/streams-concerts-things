from bs4 import BeautifulSoup
import requests
import re
# 
def scrape_royal(): 
    url = 'https://www.theroyalamerican.com/schedule/'

    data = requests.get(url)

    #print(data.text)
    if data.status_code == 200:
    # Get the HTML content from the response
        html_content = data.text
        soup = BeautifulSoup(html_content, 'html.parser')
        div_elements = soup.find_all('div', class_='eventlist-column-info')
        #for i in div_elements[0]:
            # print(i)
            # print(i.get_text(strip=True))
# Check if there are any matching div elements
        if div_elements:
            # Loop through each div element
            for div_element in div_elements:
                # Extract information from the div
                title = div_element.find('h1', class_='eventlist-title').text.strip()
                date_elements = div_element.select('ul.eventlist-meta-date time.event-date')
                times_12hr = div_element.select('ul.eventlist-meta-date time.event-time-12hr')
                # times_24hr = div_element.select('ul.eventlist-meta-date time.event-time-24hr')
                description = div_element.find('div', class_='eventlist-description').find('p').text.strip()
                #print(description)
                bands = [band.strip() for band in description.split('*') if band.strip()]

# Create a dictionary with the key "bands"
                result_dict = {"bands": bands}
                print(result_dict)

                # Split the substring by "*" to get individual parts
                #individual_parts = [part.strip() for part in substring_after_pipe.split('*')]
                #description = div_element.find('div', class_='eventlist-description')
                #print(description)
                # performer_paragraphs = description.find_all('p', class_='')
                # for i in performer_paragraphs: 
                #     print(i.text.strip())
                # for paragraph in performer_paragraphs:
                #     performers = [performer.strip() for performer in paragraph.text.split('*')]
                #     print("Performers:", performers)
                #print(description)
                #event_description_div = div_element.find('div', class_='eventlist-description')
                # view_event_link = div_element.find('a', class_='eventlist-button').get('href')

                # Organize information into JSON format for each div
                event_json = {
                    "Title": title,
                    # "Dates": [{"Day": date.text.split(',')[0], "Date": date.text.split(',')[1].strip()} for date in date_elements],
                    # "Times_12hr": [time.text.strip() for time in times_12hr],
                    # "Times_24hr": [time.text.strip() for time in times_24hr],
                     "Description": description,
                    # "ViewEventLink": view_event_link
                }

                # Print or store the resulting JSON for each div
                #print(event_json)
        else:
            print("No div elements with the specified class found.")
    
        # Loop through each element and print its text
        # for index, element in enumerate(div_element, start=1):
        #     if element.name == 'a':  # Ensure the element is an <a> tag
        #         print(f"Text inside <a> {index}: {element.text.strip()}")
        #     else:
        #         print("No div with the specified class found.")


scrape_royal()