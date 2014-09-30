
from twython import Twython, TwythonStreamer
from threading import Thread
from time import sleep
import requests
from twitter import Api

APP_KEY = "l54U8NAH75kHGYnNJ4wmR6LSe"
APP_SECRET = "JPS1r4M6TXk1dU1NqHTpGL1TuYPqQVa1XMyRFPSg4ogBNroBMd"
OAUTH_TOKEN = "2790564189-A4bTLr10wbKN3ZghY0tFILFPJL4aOF8tpHQQquo"
OAUTH_TOKEN_SECRET = "Y6TbVhGNMgwP2XZBvWKpbFpHi6wdpACW2KPmgHmUJ01Yb"

"""
https://api.twitter.com/1.1/friendships/create.json?user_id=1401881&follow=true
"""


def _add_followers(q="love"):

    stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=q)
    """while True:
        results = twitter.search(q=q)
        if results.get('statuses'):
            for result in results['statuses']:
                new_friend = result["id_str"]"""
        
    

class MyAPI(Api):
    
    def follow(self, user_id):    
        url = "https://api.twitter.com/1.1/friendships/create.json?user_id=%s&follow=true" %user_id
        self._RequestUrl(url, 'POST', data={})
        
class MyStreamer(TwythonStreamer):
    myApi = MyAPI(consumer_key=APP_KEY, consumer_secret=APP_SECRET,access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)
    
    def on_success(self, data):
        if 'user' in data and "id_str" in data["user"]:
           self.myApi.follow(data["user"]['id_str'])

    def on_error(self, status_code, data):
        sleep(3)
        
if __name__ == "__main__":
    myApi = MyAPI(consumer_key=APP_KEY, consumer_secret=APP_SECRET,access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)
    #myApi.follow("306340940")
    #_add_followers("love")
    
    t1 = Thread(target = _add_followers, args = ("love", ))
    t1.start()
    
    t2 = Thread(target = _add_followers, args = ("happy", ))
    t2.start()
    
    t3 = Thread(target = _add_followers, args = ("sad", ))
    t3.start()
    
    t4 = Thread(target = _add_followers, args = ("feelings", ))
    t4.start()

    t5 = Thread(target = _add_followers, args = ("family", ))
    t5.start()
    
    t6 = Thread(target = _add_followers, args = ("friends", ))
    t6.start()

    t7 = Thread(target = _add_followers, args = ("facebook", ))
    t7.start()
    
    t8 = Thread(target = _add_followers, args = ("instagram", ))
    t8.start()

    t9 = Thread(target = _add_followers, args = ("crazy", ))
    t9.start()
    
    
    t10 = Thread(target = _add_followers, args = ("amor", ))
    t10.start()
    
    t12 = Thread(target = _add_followers, args = ("faliz", ))
    t12.start()
    
    t13 = Thread(target = _add_followers, args = ("triste", ))
    t13.start()
    
    t14 = Thread(target = _add_followers, args = ("hijos", ))
    t14.start()

    t15 = Thread(target = _add_followers, args = ("familia", ))
    t15.start()
    
    t16 = Thread(target = _add_followers, args = ("amigos", ))
    t16.start()

    t17 = Thread(target = _add_followers, args = ("twitter", ))
    t17.start()
    
    t18 = Thread(target = _add_followers, args = ("sentimientos", ))
    t18.start()

    t19 = Thread(target = _add_followers, args = ("locura", ))
    t19.start()