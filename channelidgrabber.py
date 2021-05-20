#some thing to do with yotube videos
from googleapiclient import discovery
import json
#https://www.youtube.com/watch?v=coZbOM6E47I
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

youtube = discovery.build("youtube","v3",developerKey=API_KEY)

#request = youtube.channels().list(part="snippet,contentDetails,statistics",id="UCCezIgC97PvUuR4_gbFUs5g")
request = youtube.videos().list(part="snippet,contentDetails,snippet,statistics",id="coZbOM6E47I")
response = request.execute()

print(response)


def channelIdGrabber():
    return

