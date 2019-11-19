import os
from twython import Twython


class TwitterAPI(object):

    def __init__(self):
        self.twitter = Twython(
            os.environ['TWITTER_APP_KEY'],
            os.environ['TWITTER_APP_SECRET'],
            os.environ['TWITTER_OAUTH_TOKEN'],
            os.environ['TWITTER_OAUTH_TOKEN_SECRET']
        )
