# importing the libraries 
from bs4 import BeautifulSoup 
import requests 
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# creating function 
def scrape_info(url): 
	
	# getting the request from url 
	r = requests.get(url) 
	
	# converting the text 
	s = BeautifulSoup(r.text, "html.parser") 
	
	# finding meta info for title 
	title = s.find("span", class_="watch-title").text.replace("\n", "") 
	
	# finding meta info for views 
	views = s.find("div", class_="watch-view-count").text 
	
	# finding meta info for likes 
	likes = s.find("span", class_="like-button-renderer").span.button.text 
	
	# saving this data in dictionary 
	data = {'title':title, 'views':views, 'likes':likes} 
	
	# returning the dictionary 
	return data 

# main function 
# if __name__ == "__main__": 
	
# 	# URL of the video 
# 	url ="https://www.youtube.com/watch?time_continue=17&v=2wEA8nuThj8"
	
# 	# calling the function 
# 	data = scrape_info(url) 
	
# 	# printing the dictionary 
# 	print(data) 


#sGET https://www.googleapis.com/youtube/v3/search?key={your_key_here}&channelId={channel_id_here}&part=snippet,id&order=date&maxResults=20


DEVELOPER_KEY = 'AIzaSyBojdanEe9sdgK1hdspp2pYaHoupzOYRFU'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search():
    videos = []
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
    response = youtube.channels().list(
        part="contentDetails",
        id="UCy64jj2RTOM8lILQNGHF02A"
        ).execute()
    print(response)
    playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Retrieve videos from the playlist
    playlist_items = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50  # Set the maximum number of results per request
    ).execute()
    #print(playlist_items)
    while playlist_items:
        videos.extend(playlist_items["items"])
        next_page_token = playlist_items.get("nextPageToken")
        if next_page_token:
            playlist_items = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()
        else:
            break

    return videos
vids = youtube_search()
for video in vids:
        title = video["snippet"]["title"]
        views = video["statistics"]["viewCount"]
        print(f"Video Title: {title}")
        print(f"Views: {views}")
        