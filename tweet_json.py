from flask import Flask, render_template, send_file
import tweepy, json
(consumer_key, consumer_secret,access_token, access_token_secret) = ("QlPFb8JZa0necEyeW6LxtQbdi","cfRifjTTGVL2aTZLcQV2WBjwBETm9r4W4vgaL3Dawar9Hx4aUS","231684476-R7CjopUfvvvCGvj4woGYabIBGa0a5XFZnzQhyhTp","GW6TpmVIqGijvlP9EX8FNy5jaijlKTpOn3VCxJEXPWyRr")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
    data = []
    for status in tweepy.Cursor(api.user_timeline, id="PakShowbizc").items(100):
        tweet = {"text": status.text}
        if status.entities.get("hashtags") != None and not len(status.entities.get("hashtags")) < 1:
            tweet["hashtags"] = [{"text":x["text"]} for x in status.entities.get("hashtags")]
        data.append(tweet)
    return render_template("index.html",data=data)



@app.route("/trends", methods=['GET'])
def trends():
    #trends1 = api.trends_place(2211096) # from the end of your code
    trends1 = api.trends_place(1) # from the end of your code
    return json.dumps(trends1)


app.run(host="127.0.0.1", port=3000)