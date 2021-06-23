#some thing to do with yotube playlistItems
from googleapiclient import discovery
import json
#https://www.youtube.com/watch?v=coZbOM6E47I
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

youtube = discovery.build("youtube","v3",developerKey=API_KEY)

#request = youtube.channels().list(part="snippet,contentDetails,statistics",id="UCCezIgC97PvUuR4_gbFUs5g")
request = youtube.playlistItems().list(part="contentDetails,snippet",
                                       playlistId="UUfzlCWGWYyIQ0aLC5w48gBQ",
                                       maxResults=50)
response = request.execute()

print(response)
