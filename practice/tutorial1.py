#some thing to do with yotube channel
from googleapiclient import discovery
import json

API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

youtube = discovery.build("youtube","v3",developerKey=API_KEY)

#request = youtube.channels().list(part="snippet,contentDetails,statistics",id="UCCezIgC97PvUuR4_gbFUs5g")
request = youtube.channels().list(part="snippet,contentDetails,statistics",forUsername="sentdex")
response = request.execute()

print(response)