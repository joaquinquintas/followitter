
from twython import Twython, TwythonStreamer
from threading import Thread
from time import sleep
import requests


APP_KEY = "TxZsGIyB7YUQiP1nHglOipwUR"
APP_SECRET = "j5uN23qtXxUuwxJKfb3ue5qsSSpHFThDk4DA80mbji6CU4isEM"
OAUTH_TOKEN = "2790564189-uL1jLjx1ZrdXpTwtnmSFHQDO8D4oFbsp8nyMb2r"
OAUTH_TOKEN_SECRET = "WSVvqpqzGfWp1vjr4XPcKSue2OHu17K5PQfMlIAsZAeuR"

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
        
        

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'id_str' in data:
            post_data = "https://api.twitter.com/1.1/friendships/create.json?user_id=%s&follow=true" %data['id_str']

    def on_error(self, status_code, data):
        sleep(3)
        
if __name__ == "__main__":
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
