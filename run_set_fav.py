
from twython import Twython, TwythonStreamer
from threading import Thread
from time import sleep
import requests
import twitter

APP_KEY = "l54U8NAH75kHGYnNJ4wmR6LSe"
APP_SECRET = "JPS1r4M6TXk1dU1NqHTpGL1TuYPqQVa1XMyRFPSg4ogBNroBMd"
OAUTH_TOKEN = "2790564189-A4bTLr10wbKN3ZghY0tFILFPJL4aOF8tpHQQquo"
OAUTH_TOKEN_SECRET = "Y6TbVhGNMgwP2XZBvWKpbFpHi6wdpACW2KPmgHmUJ01Yb"

    
if __name__ == "__main__":
    myApi = twitter.Api(consumer_key=APP_KEY, consumer_secret=APP_SECRET,access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)
    
    
    while True:
        timeline = []
        try:
            timeline = myApi.GetHomeTimeline()
        except Exception, e:
            print e
            sleep(40)
        for t in timeline:
            try:
                myApi.CreateFavorite(status=t)
                print t
            except:
                sleep(10)
        sleep(10)

    