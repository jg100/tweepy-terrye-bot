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
    while True:

        now = datetime.now()
        current_time = now.strftime("%H:%M")

        rand_hour = random.randint(1, 22)
        rand_min = random.randint(1, 59)

        str_rand_hour = "0" + str(rand_hour) if rand_hour < 12 else str(rand_hour)
        str_rand_minute = "0" + str(rand_min) if rand_min < 12 else str(rand_min)

        time.sleep(10)
        print("Random time has been generated. 10 Second Cool Down has begun...")

        rand_time = str_rand_hour + ":" + str_rand_minute

        logger.info("Current Time =" + current_time)
        logger.info("Random Hour Generated: " + rand_time)

        if str(current_time) == rand_time:
            logger.info(f"Current time matches random hour")
            time.sleep(3)
            tweet_file = open("tweets_database.txt", "r")
            time.sleep(2)
            logger.info(f"Data file has been opened...")
            time.sleep(2)
            tweets_list = list()

            for x in tweet_file:
                tweets_list.append(x)

            tweet_file.close()

            tweet = tweets_list[random.randint(0, len(tweets_list) - 1)]
            print(tweet)
            time.sleep(2)
            # Update status
            try:
                api.update_status(status=tweet)
                logger.info(f"\'" + tweet + '\'' + " has been posted")
                time.sleep(random.randint(10000, 21600))  # Sleep for 4-5hrs hours
                continue
            except tweepy.TweepError as error:
                logger.error(f"Error has ocured in posting: " + str(ValueError))
                if error.api_code == 187:
                    print('Duplicate message')
                    time.sleep(3)
                    continue
            # print(tweet)


if __name__ == "__main__":
    main()
