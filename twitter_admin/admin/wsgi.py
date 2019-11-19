import logging
import sys

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from twitter_admin.admin.admin import TwitterUsersModelView
from twitter_admin.database import session_scope, create_database
from twitter_admin.models import TwitterUsers, Tags

logging.basicConfig(stream=sys.stderr)

app = Flask(__name__)
app.debug = True
app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True

create_database()

with session_scope() as session:
    admin = Admin(app,
                  name='Admin',
                  template_mode='bootstrap3',
                  url='/',
                  index_view=TwitterUsersModelView(TwitterUsers, session))
    admin.add_view(ModelView(Tags, session))
