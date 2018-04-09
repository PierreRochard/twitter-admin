import json
import os

from database import session_scope
from models import TwitterUsers

path = 'followers'
followers = []
for doc in os.listdir(path):
    with open(os.path.join(path, doc), 'r') as fp:
        follower = json.load(fp)
        followers.append(follower)

# Make this upsert
for index, follower in enumerate(followers):
    print(round(index/len(followers), 4)*100)
    new_twitter_user = TwitterUsers()
    for key, value in follower.items():
        setattr(new_twitter_user, key, value)
    with session_scope() as session:
        session.add(new_twitter_user)
