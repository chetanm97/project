import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import twappconfig as tw
import json

class listener(StreamListener):

    c=0
    tweet_text=[]
    ht=[]
    locot=[]

    def on_data(self,data):
        d1=json.loads(data)
        self.tweet_text.append(d1['text'])
        print(self.c)
        self.c=self.c+1
        if self.c%3 == 0 and self.c!=0:
            self.locot.append(self.tweet_text)
            self.tweet_text=[]
            return False
        return True

    def on_error(self,status):
        print(status)


def pre_class():

    ht=[]

    auth = OAuthHandler(tw.ckey,tw.csecret)
    auth.set_access_token(tw.akey,tw.asecret)
    api = tweepy.API(auth)
    trends1 = api.trends_place(23424848)
    twitterStream = Stream(auth, listener())



    for ele in trends1:
        for el in ele['trends']:
            ht.append(el['name'])
    x=0
    for hastag in ht:
        twitterStream.filter(track=[hastag])

    return listener.locot,ht
