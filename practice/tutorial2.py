#some thing to with channel playlists and pagetokens
from googleapiclient import discovery
import json

API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

youtube = discovery.build("youtube","v3",developerKey=API_KEY)

pl_request = youtube.playlists().list(
    part="contentDetails,id,snippet,status",
    channelId="UCCezIgC97PvUuR4_gbFUs5g",
    pageToken=None)

response = pl_request.execute()

print(response)