import tweepy
import logging
from config import create_api
import time

import responses

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            status_text = responses.process_response(tweet.text)

            # here is the area to add randomly generated responses.
            api.update_status(
                status=status_text + " " + tweet.user,
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["hello", "biology", "hi", "remember", "school", "hello", "how", "a", "when"],
                                  since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
