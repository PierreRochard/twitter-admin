from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from database import session_scope
from models import TwitterUsers

app = Flask(__name__)
app.debug = True


class TwitterUsersModelView(ModelView):
    def __init__(self, model, session, *args, **kwargs):
        super(TwitterUsersModelView, self).__init__(model, session, *args, **kwargs)
        self.static_folder = 'static'
        self.endpoint = 'admin'
        self.name = 'Admin'

    can_delete = False
    can_create = False
    can_edit = False
    can_view_details = True
    column_searchable_list = ['screen_name', 'name', 'description', 'description']
    column_list = [
        'screen_name',
        'name',
        'description',
        'location',
        'following',
        'created_at',
        'followers_count',
        'friends_count',
        'statuses_count',
        'favourites_count',
        'lang',
    ]
    page_size = 50


with session_scope() as session:
    admin = Admin(app,
                  name='Admin',
                  template_mode='bootstrap3',
                  url='/',
                  index_view=TwitterUsersModelView(TwitterUsers, session))

app.run()
