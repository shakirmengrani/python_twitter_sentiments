import tweepy
(consumer_key, consumer_secret,access_token, access_token_secret) = ("QlPFb8JZa0necEyeW6LxtQbdi","cfRifjTTGVL2aTZLcQV2WBjwBETm9r4W4vgaL3Dawar9Hx4aUS","231684476-R7CjopUfvvvCGvj4woGYabIBGa0a5XFZnzQhyhTp","GW6TpmVIqGijvlP9EX8FNy5jaijlKTpOn3VCxJEXPWyRr")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trends1 = api.trends_place(2211096) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)