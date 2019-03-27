import tweepy
import twappconfig as tw
from tweepy import OAuthHandler
import json
auth = OAuthHandler(tw.ckey,tw.csecret)
auth.set_access_token(tw.akey,tw.asecret)
api = tweepy.API(auth)
count=0
for tweet in tweepy.Cursor(api.search,q="#modi",rpp=1,result_type="recent",include_entities=True,lang="en").items(10):
    count+=1
    for ele in tweet.entities['hashtags']:
        print(ele)
    print("\n")
