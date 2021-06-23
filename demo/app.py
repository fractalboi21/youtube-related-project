from flask import Flask, request, redirect, render_template
import json
from videos import getParsedJsonResponse
app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"

@app.route("/meta_tags/<videoid>",methods=["GET","POST"])
def metatags(videoid):
    tags = getParsedJsonResponse(videoid)["meta_tags"]
    tags = " ".join(tags).replace("r/","")
    print(tags)
    return render_template("meta_tags.html",tags=json.dumps(tags))

