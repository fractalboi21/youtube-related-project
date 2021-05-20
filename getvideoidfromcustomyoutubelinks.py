# https://m.youtube.com/watch?v=TV2F06Pd-Dg
# https://m.youtube.com/watch?v=s1J-DB2P4uU
# https://m.youtube.com/watch?v=s1J-DB2P4uU
# https://m.youtube.com/watch?v=sW9npZVpiMI
# https://youtu.be/dRcs98Zmfi4
# https://youtu.be/4EgOR8ALCHE
# https://youtu.be/Mpf4ntp0YJs
# https://youtu.be/v4sCCVinN-U
# https://youtu.be/owe9cPEdm7k
# https://youtu.be/PJYWANz2-fA
# https://www.youtube.com/watch?v=aKOJGzNEnlc
# https://www.youtube.com/watch?v=AhAay4FT-nE
# https://www.youtube.com/watch?v=B1ouIlaGlQg
# https://www.youtube.com/watch?v=7qz9E4KUJ4w
# https://www.youtube.com/watch?v=DVQ29IkEmM0

def file_to_list(path):
    lst = []
    with open(path,"r") as f:
        f = f.read().split("\n")
        
        
        for i in f:
            if i != '':
                lst.append(i)
        return lst

links = file_to_list("/home/pi/Documents/youtube api tutorial/youtubevideolinks.txt")

def getVideoIdFromYoutubeLink(url):
    url = url.split("//")[1].split("/")[-1]
    if url[0:8] == "watch?v=":
        urlwv = url.split("=")[1]
        return urlwv
    else:
        return url

for link in links:
    print(getVideoIdFromYoutubeLink(link))
