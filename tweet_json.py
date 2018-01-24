from flask import Flask, render_template, send_file
try:
  from flask_headers import headers
except:
  from flask.ext.headers import headers

import tweepy, json
(consumer_key, consumer_secret,access_token, access_token_secret) = ("XBNDfgtLtZWP8We3iY2zX8M8D","faGgaP83nYVrV7YUr6MXgndvQzZWJmvtCBQFKfnDAFgsXVcsNi","377205991-w9F2zr1MFC6pbIQfes7T1a1aIJPxkf8vGnbzd6KB","CT74MtgggLx4hD6ois6QSHxtMJlmXODSleytqisFZrt9S")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
app = Flask(__name__)

@app.route("/", methods=['GET'])
# @headers({'Content-Type': 'application/json'})
def index():
    data = []
    for status in api.home_timeline(): # tweepy.Cursor(api.user_timeline, id="mashable").items(100):
        tweet = {"text": status.text}
        if status.entities.get("hashtags") != None and not len(status.entities.get("hashtags")) < 1:
            tweet["hashtags"] = [{"text":x["text"]} for x in status.entities.get("hashtags")]
        data.append(tweet)
    # return data
    return render_template("index.html",data=data)

@app.route("/trends", methods=['GET'], defaults={'id': None})
@app.route("/trends/<id>", methods=['GET'])
@headers({'Content-Type': 'application/json'})
def trends(id):
    if id: 
        trends1 = api.trends_place(id)
        return json.dumps(trends1)
    else:
        data = []
        for x in api.trends_available():
            data.append({'woeid': x['woeid'], 'name': x['name'], 'country': x['country'], 'countryCode': x['countryCode']})
        return json.dumps(data)

app.run(host="127.0.0.1", port=3000)