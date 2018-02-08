import sys
import datetime 
from time import sleep
import tweepy


# Ensure Python 3 is running
if sys.version_info[0] < 3:
    raise Exception("Designed to only run on Python 3")


CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'


TWEET_LENGTH = 280  # if Twitter ever changes the tweet length, modify if here
#  might remove the TWEET_LENGTH parameter in future version


TWEET_LIST_FILE = '2018.txt'  # file we are reading our tweets from


RUN_EVERY_N_HOURS = 24
RUN_TIMER = RUN_EVERY_N_HOURS*(60*60)  # 24*(60*60) == 24 hours x (60 seconds per 60 mins)


def get_date():
    today_date = datetime.date.today()
    return today_date


def read_tweet_list():
    with open(TWEET_LIST_FILE) as fp:  
        line = fp.readline()
    while line:
        if str(today_date) in line[0:10]:
            print(line[11:])












# Part that actually makes the tweet
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status('Updating using OAuth authentication via Tweepy!')


# Get daily tweet from text file
def get_daily_tweet():
    with open(TWEET_LIST_FILE) as f:
    for line in f:
        if today in line:
             line = 
    events = this_day.section("Events") # unicode
    # split unicode into list items
    lines = events.split('\n')
    # get random item in list
    item_index = random.randrange(len(lines))
    event_text = lines[item_index]
    # tweet the whole sentence if it's short enough
    if len(event_text) <= TWEET_LENGHT:
        return event_text
    # otherwise just print the first 137 characters plus "..." = 140
    else:
        return event_text[0:137] + "..."

"""
import datetime as d
today = d.date.today()
if str(today) in ['2018-02-08']:
...   print("yep!")
"""

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
