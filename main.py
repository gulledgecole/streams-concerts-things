import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP GET request to the artist's Spotify URL
artist_url = "https://open.spotify.com/artist/4nUBBtLtzqZGpdiynTJbYJ"
response = requests.get(artist_url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract song names and stream counts for the top 10 songs
    song_names = []
    stream_counts = []
    #songs = soup.find_all('div', class_='Type__TypeElement-sc-goli3j-0 ieTwfQ nYg_xsOVmrVE_8qk1GCW', attrs={'data-encore-id': 'type'})
    songs = soup.find_all('data-encore-id')
    number = soup.find_all(string="342,502")
    test = soup.find_all(class_ = "Type__TypeElement-sc-goli3j-0 ieTwfQ nYg_xsOVmrVE_8qk1GCW")
    print(songs)

    #print(songs)
    counts = soup.find_all('span', class_='second-line')
    for song, count in zip(songs[:10], counts[:10]):
        song_names.append(song.text)
        stream_counts.append(count.text)

    # Create a pandas DataFrame with the scraped data
    data = {'Song Name': song_names, 'Stream Count': stream_counts}
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)

    # You can also save the data to a CSV file if needed
    # df.to_csv('spotify_stream_counts.csv', index=False)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
