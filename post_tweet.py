import tweepy
import pyrebase
(consumer_key, consumer_secret,access_token, access_token_secret) = ("QlPFb8JZa0necEyeW6LxtQbdi","cfRifjTTGVL2aTZLcQV2WBjwBETm9r4W4vgaL3Dawar9Hx4aUS","231684476-R7CjopUfvvvCGvj4woGYabIBGa0a5XFZnzQhyhTp","GW6TpmVIqGijvlP9EX8FNy5jaijlKTpOn3VCxJEXPWyRr")
config = {
  "apiKey": "AIzaSyDdIGTl198sqjqzTVSud1gYEwvH_tpWXbg",
  "authDomain": "teachingbot-b50d1.firebaseapp.com",
  "databaseURL": "https://teachingbot-b50d1.firebaseio.com",
  "storageBucket": "teachingbot-b50d1.appspot.com"
}
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
firebase = pyrebase.initialize_app(config)
api = tweepy.API(auth)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("shakir.mengrani@gmail.com", "Shakir@786")
for status in tweepy.Cursor(api.user_timeline, id="bbcworld").items(1000):
    tweet = {}
    tweet["text"] = status.text
    if status.entities.get("hashtags") != None and not len(status.entities.get("hashtags")) < 1:
        tweet["hashtags"] = [x["text"] for x in status.entities.get("hashtags")]
    db.child("data").push(tweet,user['idToken'])