#some thing to do with yotube comments
from googleapiclient import discovery
import json
#https://www.youtube.com/watch?v=coZbOM6E47I
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

youtube = discovery.build("youtube","v3",developerKey=API_KEY)

#request = youtube.channels().list(part="snippet,contentDetails,statistics",id="UCCezIgC97PvUuR4_gbFUs5g")
request = youtube.commentThreads().list(part="snippet,replies",videoId="coZbOM6E47I",maxResults=50,textFormat="plainText")
response = request.execute()

print(response)