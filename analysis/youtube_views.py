# importing the libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.cloud import secretmanager

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def get_key():
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/639888050178/secrets/youtube-key/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    return payload


def youtube_search(payload):
    videos = []
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=payload)
    response = (
        youtube.channels()
        .list(part="contentDetails", id="UCy64jj2RTOM8lILQNGHF02A")
        .execute()
    )
    playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Retrieve videos from the playlist
    playlist_items = (
        youtube.playlistItems()
        .list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,  # Set the maximum number of results per request
        )
        .execute()
    )
    while playlist_items:
        videos.extend(playlist_items["items"])
        next_page_token = playlist_items.get("nextPageToken")
        if next_page_token:
            playlist_items = (
                youtube.playlistItems()
                .list(
                    part="snippet",
                    playlistId=playlist_id,
                    maxResults=50,
                    pageToken=next_page_token,
                )
                .execute()
            )
        else:
            break

    return videos


def get_views(videos, payload):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=payload)
    for vid in videos:
        title = vid["snippet"]["title"]
        published = vid["snippet"]["publishedAt"]
        id = vid["snippet"]["resourceId"]["videoId"]
        stats = youtube.videos().list(part="statistics", id=id).execute()
        views = stats["items"][0]["statistics"]["viewCount"]
        print(views)

    return views


if __name__ == "__main__":
    payload = get_key()
    videos = youtube_search(payload)
    views = get_views(videos, payload)
