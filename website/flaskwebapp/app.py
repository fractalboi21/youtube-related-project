from flask import Flask, render_template, request, redirect, url_for
from videos import getParsedJsonResponse
from getvideoidfromcustomyoutubelinks import getVideoIdFromYoutubeLink

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "welcome to my youtube channel!"




@app.route('/getvideoinfo',methods = ['POST', 'GET'])
def getvideoinfo():
   if request.method == 'POST':
      video_link = request.form['videolink']
      video_id = getVideoIdFromYoutubeLink(video_link)
      response = getParsedJsonResponse(video_id)
      tags = response["meta_tags"]
      
      return render_template('display.html',response = response, tags=tags)
   else:
      return render_template("getvideoinfo.html")
