import re
import requests

playListId="UU2-slOJImuSc20Drbf88qvg"
url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId={playListId}&key=AIzaSyDhzUyksZsIN-OsKTMNdDs_yh0_khuV90Y&maxResults=50"

lst = []

for i in range(50):
    ##print(res.get("items")[i].get("contentDetails").get("videoId"))
    pass
#get all page tokens from youtube playlistItem api endpoint

# send request to url and 
def doesNextPageTokenExist(url):
    pass

# get nextpagetoken 
def getNextPageToken():
    return

def getAllNexTPageTokens(url):
    req = requests.get(url)
    res = req.json()
    pgtkn = res.get("nextPageToken")
    currul = bool(pgtkn)
    while bool(currul):
        print("next page token exist!"+res.get("nextPageToken"))
        



getAllNexTPageTokens("https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId=UU2-slOJImuSc20Drbf88qvg&key=AIzaSyDhzUyksZsIN-OsKTMNdDs_yh0_khuV90Y&maxResults=50")