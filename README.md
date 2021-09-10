# youtube-related-project
tools that i made using youtube data api v3 and python3.

some useful links:
https://github.com/amastis/YouTube-data-scraper

playlist item response
```
https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&part=contentDetails&part=status&part=id&maxResults=50&playlistId=PLdPBL8cOjdzWQOdmxe6jhA5bhiKtxW0Oj&key=[YOUR_API_KEY]
```

playlist response
```
https://youtube.googleapis.com/youtube/v3/playlists?part=contentDetails&part=snippet&channelId=UCCWp4CCmI2JmIaoAuv0ocEA&key=[YOUR_API_KEY]
```

video response
```
https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=snippet&part=snippet&id=sW9npZVpiMI&prettyPrint=true&key=[YOUR_API_KEY]
```
search response
```
https://youtube.googleapis.com/youtube/v3/search?part=snippet&q=helloworld&key=[YOUR_API_KEY]
```
comment threads response
```
https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&part=replies&videoId=sW9npZVpiMI&key=[YOUR_API_KEY]
```
channles response
```
https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&part=contentDetails&part=statistics&id=UC4JX40jDee_tINbkjycV4Sg&key=[YOUR_API_KEY]
```

