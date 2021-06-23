from googleapiclient import discovery
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"
youtube = discovery.build("youtube","v3",developerKey=API_KEY)

#get channel info
def getChannelInfo(channel_id):
  request = youtube.channels().list(part="contentDetails,snippet,statistics", id=channel_id)
  response = request.execute()
  return response

#get playlists info
def getPlaylistItemsInfo(playlist_id,page_token):
  request = youtube.playlistItems().list(part="contentDetails",playlistId=playlist_id,pageToken=page_token)
  response = request.execute()
  return response

getChannelInfo("UC4JX40jDee_tINbkjycV4Sg")

#get all the video
playlist_id = "UU4JX40jDee_tINbkjycV4Sg"
page_token=None
video_id_list = []
while True:

  response = getPlaylistItemsInfo(playlist_id, page_token)
  items = response["items"]

  for vidid in items:
    video_id_list.append(vidid["contentDetails"]["videoId"])
  

  if "nextPageToken" in response:
    page_token = response.get("nextPageToken")
    
    response = getPlaylistItemsInfo(playlist_id, page_token)
    items = response["items"]
    

  
  else:
    break

l = len(video_id_list)
print(l)
for i in video_id_list:
  print(i)
