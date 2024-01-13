from imports import *


def scrape_snug(url):
    user_agents_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    ]
    data = requests.get(url, headers={"User-Agent": random.choice(user_agents_list)})
    if data.status_code == 200:
        html_content = data.text
        soup = BeautifulSoup(html_content, "html.parser")

        div_elements = soup.find_all("div", class_="wp-block-media-text__content")

        # Iterate through each div element
        for div_element in div_elements:
            # Find all strong elements within the div
            bands = div_element.find_all("strong")
            clean_bands_list = []
            # Iterate through each strong element. There's a couple bullshit ones we can't do anything about, not worth it.
            for band in bands:
                # Extract text, remove "w/" and strip spaces
                modified_item = band.text.replace("w/ ", "").strip()

                # Check if "21" or "18" is not in the modified item, sometimes a fucklin w slips through.
                if (
                    "21" not in modified_item
                    and "18" not in modified_item
                    and "w/" not in modified_item
                ):
                    # Append to the clean bands list
                    clean_bands_list.append(modified_item)
            dates = div_element.find(
                "p", class_="has-text-align-center has-large-font-size"
            ).text.strip()
            dates = helpers.date_handler(dates)
            print(dates)


scrape_snug("https://snugrock.com/")
