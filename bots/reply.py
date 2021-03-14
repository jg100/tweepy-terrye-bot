import tweepy
import logging
from config import create_api
import time

import responses

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        print("Tweet: " + tweet.text + "\nstatus ID: " + str(tweet.in_reply_to_status_id))

        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue

        logger.info(f"Answering to {tweet.user.name}")

        if not tweet.user.following:
            tweet.user.follow()

        status_text = responses.process_response(tweet.text)
        print("Status test: " + status_text + " @" + str(tweet.user.screen_name))

        # here is the area to add randomly generated responses.
        try:
            api.update_status(
                status=status_text + " " + "@" + str(tweet.user.screen_name),
                in_reply_to_status_id=tweet.id,
            )
        except tweepy.TweepError as error:
            logger.error(f"Error has ocured in posting: " + str(ValueError))
            time.sleep(1)
            if error.api_code == 187:
                print('Duplicate message')

                status_text = responses.process_response("random response")

                api.update_status(
                    status=status_text + " " + "@" + str(tweet.user.screen_name),
                    in_reply_to_status_id=tweet.id,
                )

            if error.api_code == 107:
                print("Message too long")
                time.sleep(1)
                continue
    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api,
                                  since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
