
import re
import requests
"""
first send request without page token 
then get nextPageToken from intial response
send request with new nextPageToken from secont response
"""

urlWithOutPageToken = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet, contentDetails&playlistId=UUsBjURrPoezykLs9EqgamOA&key=AIzaSyDhzUyksZsIN-OsKTMNdDs_yh0_khuV90Y&maxResults=50&pageToken="

def responseUrlNextPageToken(pageToken):
    urlWithPageToken = urlWithOutPageToken+pageToken
    response = requests.request("GET",urlWithPageToken)
    return response.json()



# print(responseUrlNextPageToken("EAAaBlBUOkNESQ"))

itemsList = []
initialRequest = requests.request("GET",urlWithOutPageToken).json()
initalNextPageToken = initialRequest.get("nextPageToken")

pageTokenTracker = requests.request("GET",urlWithOutPageToken).json().get("nextPageToken")
# send request as long as the response object contains nextPageToken


