from datetime import datetime
import json
import logging
import os
import time

from twython import Twython, TwythonRateLimitError

logging.basicConfig(
    level=logging.INFO,
    filename='twitter.log',
    format='%(asctime)s %(levelname)s: %(message)s'
)

if not os.path.exists('followers'):
    os.makedirs('followers')


class FollowerGetter(object):
    twitter = Twython(os.environ['TWITTER_APP_KEY'],
                      os.environ['TWITTER_APP_SECRET'],
                      os.environ['TWITTER_OAUTH_TOKEN'],
                      os.environ['TWITTER_OAUTH_TOKEN_SECRET']
                      )

    cursor = -1

    def get_followers_list(self):
        followers = self.twitter.get_followers_list(
            screen_name='pierre_rochard',
            include_user_entities=True,
            count=200,
            cursor=self.cursor)
        self.cursor = followers['next_cursor']
        logging.info(f'next_cursor: {self.cursor}')
        for follower in followers['users']:
            with open(f'followers/{follower["id"]}.json', 'w') as fp:
                json.dump(follower, fp, indent=4)

    def get_all_followers(self):
        while True:
            try:
                self.get_followers_list()
            except TwythonRateLimitError as e:
                retry_after = int(e.retry_after)
                now = datetime.now().timestamp()
                seconds = retry_after - now
                logging.info(f'sleeping for {round(seconds/60)} minutes')
                time.sleep(seconds + 5)


FollowerGetter().get_all_followers()
