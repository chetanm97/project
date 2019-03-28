import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import twappconfig as tw
import json



def pre_class():

    ht=[]
    locot=[]
    t_w=[]

    auth = OAuthHandler(tw.ckey,tw.csecret)
    auth.set_access_token(tw.akey,tw.asecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    #trends1 = api.trends_place(23424848)



    #for ele in trends1:
    #    for el in ele['trends']:
    #        ht.append(el['name'])
    hastag='#modi'
    #for hastag in ht:
    for tweet in tweepy.Cursor(api.search,q=hastag,rpp=1,result_type="recent",include_entities=True,lang="en").items(100):
        t_w.append(tweet.text)
    locot.append(t_w)

    return locot,ht
