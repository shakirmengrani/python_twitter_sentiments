import tweepy
(consumer_key, consumer_secret,access_token, access_token_secret) = ("XBNDfgtLtZWP8We3iY2zX8M8D","	faGgaP83nYVrV7YUr6MXgndvQzZWJmvtCBQFKfnDAFgsXVcsNi","377205991-w9F2zr1MFC6pbIQfes7T1a1aIJPxkf8vGnbzd6KB","CT74MtgggLx4hD6ois6QSHxtMJlmXODSleytqisFZrt9S")
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