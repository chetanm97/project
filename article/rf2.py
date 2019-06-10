import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import twappconfig as tw
import json




l1=['#bjp','#modi','#chowkidar','#sankalppatra']
auth = OAuthHandler(tw.ckey,tw.csecret)
auth.set_access_token(tw.akey,tw.asecret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True)
try:
    for h in l1:
        for tweet in tweepy.Cursor(api.search,q=h,rpp=100,result_type="recent",include_entities=True,lang="en").items(2000):
            with open('rfdata.txt','a') as f:
                s='{text:'+tweet.text+',label:BJP}'
                f.write(s)
except Exception as e: print(e)