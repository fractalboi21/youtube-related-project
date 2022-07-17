import requests


videoTitles = []


def getVideoTitleByYoutubeId(videoId):
    response = requests.request("GET",f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet, contentDetails, statistics&id={videoId}&key=AIzaSyDhzUyksZsIN-OsKTMNdDs_yh0_khuV90Y")
    res = response.json()
    return res.get("items")[0].get("snippet").get("title")


with open("./vididlst.txt","r") as f:
    content = f.read()

for i in content.split("\n"):
    insCont = getVideoTitleByYoutubeId(i)
    try:
        with open("FreecodecampVideoTitles.txt","a",encoding="utf-8") as wf:
            wf.write(insCont+"\n")
    finally:
        print("something went wrong!")
    
