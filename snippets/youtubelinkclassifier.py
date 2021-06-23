"""
Types of youtube links:
>videos
>playlist
>channel
"""

url = "https://m.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK"

def ResponsiveLinksClassifier(url):
    url
    if url == "https://m":
        print("looks like youtube webpage for mobile devices..")
        return "mw"
    elif url == 1:
        pass

#https://m.youtube.com/watch?v=TV2F06Pd-Dg
#https://youtu.be/dRcs98Zmfi4
#https://www.youtube.com/watch?v=AhAay4FT-nE

def youtubeLinkClassifier(url):
    urls1 = url.split("/")
    urls2 = url.split("/")[-1].split("?")[0]
    if url[2] == "":
    pass

    