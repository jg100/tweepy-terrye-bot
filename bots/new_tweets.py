#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py
import tweepy
import logging
from config import create_api
import time
from datetime import datetime
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    api = create_api()

    logger.info(f"Opening txt file")
    time.sleep(1)
    tweet_file = open("tweets_database.txt", "r")
    time.sleep(1)
    logger.info(f"Data file has been opened...")
    tweets_list = list()

    for x in tweet_file:
        ascii_sum = 0
        for c in x:
            ascii_sum += ord(c)

        if ascii_sum > 41:
            tweets_list.append(x)
            print(x + " ^^^ has been loaded into data set")

    tweet_file.close()
    while True:

        tweet = tweets_list[random.randint(0, len(tweets_list) - 1)]
        print("Selected tweet: " + tweet)
        time.sleep(2)
        # Update status
        try:
            api.update_status(status=tweet)
            logger.info(f"TWEET: " + tweet + "^ has been posted")
            sleep_time = random.randint(1000, 21600)
            logger.info(f"Sleep for: " + str(sleep_time) + " seconds")
            time.sleep(sleep_time) # max sleep time 6hrs
            continue
        except tweepy.TweepError as error:
            logger.error(f"Error has ocured in posting: " + str(ValueError))
            if error.api_code == 187:
                print('Duplicate message')
                time.sleep(1)
                continue
            if error.api_code == 107:
                print("Message too long")
                time.sleep(1)
                continue
        # print(tweet)


if __name__ == "__main__":
    main()
