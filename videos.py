from googleapiclient import discovery
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"
youtube = discovery.build("youtube","v3",developerKey=API_KEY)

# TV2F06Pd-Dg
# s1J-DB2P4uU
# s1J-DB2P4uU
# sW9npZVpiMI
# dRcs98Zmfi4
# 4EgOR8ALCHE
# Mpf4ntp0YJs
# v4sCCVinN-U
# owe9cPEdm7k
# PJYWANz2-fA
# aKOJGzNEnlc
# AhAay4FT-nE
# B1ouIlaGlQg
# 7qz9E4KUJ4w
# DVQ29IkEmM0

def getParsedJsonResponse(video_id):
    request = youtube.videos().list(part="snippet,contentDetails,snippet,statistics",id=video_id)
    response = request.execute()
    items = response["items"][0]
    kind = items["kind"]
    video_id = items["id"]
    #snippet
    published_date = items["snippet"]["publishedAt"]
    channel_id = items["snippet"]["channelId"]
    video_title = items["snippet"]["title"]
    video_description = items["snippet"]["description"]
    thumbnail_url = items["snippet"]["thumbnails"]["maxres"]["url"]
    channel_title = items["snippet"]["channelTitle"]
    meta_tags = items["snippet"]["tags"]
    category_id = items["snippet"]["categoryId"]
    #content details
    duration = items["contentDetails"]["duration"][2:]
    #stats
    view_count = items["statistics"]["viewCount"]
    like_count = items["statistics"]["likeCount"]
    dislike_count = items["statistics"]["dislikeCount"]
    favorite_count = items["statistics"]["favoriteCount"]
    comment_count = items["statistics"]["commentCount"]
    
    parsed_response = dict(kind=kind,
                           video_id=video_id,
                           published_date =published_date,
                           channel_id=channel_id,
                           video_title=video_title,
                           video_description=video_description,
                           thumbnail_url=thumbnail_url,
                           channel_title=channel_title,
                           meta_tags=meta_tags,
                           category_id=category_id,
                           duration=duration,
                           view_count=view_count,
                           like_count=like_count,
                           dislike_count=dislike_count,
                           favorite_count=favorite_count,
                           comment_count=comment_count)
    return parsed_response


    

    
    



