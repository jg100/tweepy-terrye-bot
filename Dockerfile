FROM python:3.7-alpine
RUN apk add build-base

COPY /bots/docker_run.sh /bots/
COPY /bots/config.py /bots/
COPY /bots/new_tweets.py /bots/
COPY /bots/reply.py /bots/
COPY /bots/responses.py /bots/
COPY /bots/tweets_database.txt bots/
COPY /bots/followforfollow.py /bots/
COPY /bots/requirements.txt bots/
RUN pip3 install -r bots/requirements.txt

WORKDIR /bots
CMD ./docker_run.sh
