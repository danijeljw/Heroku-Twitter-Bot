import sys
import datetime
from time import sleep
import tweepy
from twython import Twython

# Ensure Python 3 is running
if sys.version_info[0] < 3:
    raise Exception("Designed to only run on Python 3")

CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'
TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21

RUN_EVERY_N_HOURS = 24*(60*60) # 24*(60*60) == 24 hours x (60 seconds per 60 mins)

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_date():
    """ returns today's date as string, e.g. 'January 01' """
    today = datetime.date.today() # ex 2015-10-31
    return today.strftime("%B %d")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def main():
    handle = twitter_handle()
    USERS_TO_IGNORE.extend([x['user']['id'] for x in handle.get_favorites()])
    while True:
        message = get_message(handle)
        print message
        submit_tweet(message, handle)
        # random_favoriting(['apples', 'oranges'], handle)
        time.sleep(RUN_EVERY_N_SECONDS)

if __name__ == '__main__':
    main()
