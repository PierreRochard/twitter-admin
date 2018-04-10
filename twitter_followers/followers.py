from datetime import datetime
import json
import logging
import os
import time

from sqlalchemy.orm.exc import NoResultFound
from twython import Twython, TwythonRateLimitError

from twitter_followers.database import session_scope, create_database
from twitter_followers.models import TwitterUsers

logging.basicConfig(
    level=logging.INFO,
    filename='twitter.log',
    format='%(asctime)s %(levelname)s: %(message)s'
)


class Followers(object):
    data_path = 'followers'

    def __init__(self):
        self.twitter = Twython(os.environ['TWITTER_APP_KEY'],
                               os.environ['TWITTER_APP_SECRET'],
                               os.environ['TWITTER_OAUTH_TOKEN'],
                               os.environ['TWITTER_OAUTH_TOKEN_SECRET']
                               )
        self.cursor = -1
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        self.followers = []

    def save_json_files(self, followers_data):
        for follower_data in followers_data:
            json_path = os.path.join(self.data_path, f'{follower_data["id"]}.json')
            with open(json_path, 'w') as fp:
                json.dump(follower_data, fp, indent=4)

    def get_all_followers(self):
        while True:
            if not self.cursor:
                break
            try:
                followers_data = self.twitter.get_followers_list(
                    screen_name='pierre_rochard',
                    include_user_entities=True,
                    count=200,
                    cursor=self.cursor)
                self.save_json_files(followers_data['users'])
                self.cursor = followers_data['next_cursor']
                logging.info(f'next_cursor: {self.cursor}')
            except TwythonRateLimitError as e:
                retry_after = int(e.retry_after)
                now = datetime.now().timestamp()
                seconds = retry_after - now
                logging.info(f'sleeping for {round(seconds/60)} minutes')
                time.sleep(seconds + 5)

    def load_json_files(self):
        for doc in os.listdir(self.data_path):
            json_path = os.path.join(self.data_path, doc)
            with open(json_path, 'r') as fp:
                follower = json.load(fp)
                self.followers.append(follower)

    def upsert_followers(self):
        self.load_json_files()
        for index, follower in enumerate(self.followers):
            percent_done = round(index / len(self.followers)*100, 2)
            if not index % 50:
                logging.info(f'Upserted {percent_done}% of followers')
            self.upsert_follower(follower)

    @staticmethod
    def upsert_follower(follower_data: dict):
        with session_scope() as session:
            try:
                follower = (
                    session.query(TwitterUsers)
                    .filter(TwitterUsers.id == follower_data['id'])
                    .one()
                )
            except NoResultFound:
                follower = TwitterUsers()
                session.add(follower)

            for key, value in follower_data.items():
                setattr(follower, key, value)

    def sync_data(self):
        self.get_all_followers()
        self.upsert_followers()


if __name__ == '__main__':
    create_database()
    tf = Followers()
    tf.upsert_followers()
    tf.sync_data()
