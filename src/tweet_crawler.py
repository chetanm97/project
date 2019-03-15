

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener

f=open("twappconfig.py",'r')
i=0
c={}
for line in f:
    c[i]=line
    i=i+1


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(c[0], c[1])
auth.set_access_token(c[2],c[3])

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
		
