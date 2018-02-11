#!/usr/bin/env python
import datetime 
import sys
import os
import time
import tweepy

# Twitter API details
CONSUMER_KEY = 'replace with your key'
CONSUMER_SECRET = 'replace with your secret'
ACCESS_KEY = 'replace with your access key'
ACCESS_SECRET = 'replace with your access secret'

# Ensure Python 3 is running
if sys.version_info[0] < 3:
    raise Exception("Designed to only run on Python 3")

# Tweepy functionality
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# File to read tweets from
PRINT_FILE = '2018.txt'  # file we are reading our tweets from

# Main function
def main():
    if not os.path.isfile(PRINT_FILE):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    while True:
        with open(PRINT_FILE) as fp:
            for line in fp:
                if str(datetime.date.today()) in line:
                    api.update_status(line[11:])
                    return print(line[11:])
        time.sleep(10800) # sleep for 8 hours (in seconds)


# Run program
if __name__ == '__main__':
    main()

