from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from twitter_followers.admin.formatters import screen_name_formatter, \
    image_formatter
from twitter_followers.database import session_scope
from twitter_followers.models import TwitterUsers, Tags


class TwitterUsersModelView(ModelView):
    def __init__(self, model, session, *args, **kwargs):
        super(TwitterUsersModelView, self).__init__(model, session, *args,
                                                    **kwargs)
        self.static_folder = 'static'
        self.endpoint = 'admin'
        self.name = 'Followers'

    can_delete = False
    can_create = False
    can_edit = True
    can_view_details = True
    column_searchable_list = [
        'screen_name',
        'name',
        'description',
        'location'
    ]
    column_list = [
        'is_interesting',
        'tags',
        'profile_image_url',
        'screen_name',
        'following',
        'friends_followers_ratio',
        'name',
        'description',
        'location',
        'created_at',
        'followers_count',
        'friends_count',
        'statuses_count',
        'favourites_count',
        'lang',
    ]
    column_filters = [c for c in column_list if not c.endswith('_ratio')]
    column_editable_list = [
        'is_interesting',
        'tags'
    ]

    column_formatters = dict(
        screen_name=screen_name_formatter,
        profile_image_url=image_formatter
    )
    column_default_sort = ('followers_count', True)


if __name__ == '__main__':
    app = Flask(__name__)
    app.debug = True
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.secret_key = 'aS2MPk5uGu8PnTFLAK'
    with session_scope() as session:
        admin = Admin(app,
                      name='Admin',
                      template_mode='bootstrap3',
                      url='/',
                      index_view=TwitterUsersModelView(TwitterUsers, session))
        admin.add_view(ModelView(Tags, session))
    app.run(port=5023)
