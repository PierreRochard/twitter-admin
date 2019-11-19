from sqlalchemy import (
    BIGINT,
    Boolean,
    Column,
    DateTime,
    func,
    String,
    ForeignKey)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

Base = declarative_base()


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(BIGINT, primary_key=True)
    name = Column(String)

    def __str__(self):
        return self.name


class TwitterUsersTags(Base):
    __tablename__ = 'twitter_users_tags'
    id = Column(BIGINT, primary_key=True)
    twitter_user_id = Column(BIGINT, ForeignKey('twitter_users.id'))
    tag_id = Column(BIGINT, ForeignKey('tags.id'))


class TwitterUsers(Base):
    __tablename__ = 'twitter_users'

    record_created_at = Column(DateTime(timezone=True),
                               nullable=False,
                               server_default=func.now())

    record_updated_at = Column(DateTime(timezone=True),
                               nullable=False,
                               onupdate=func.now(),
                               server_default=func.now())

    is_interesting = Column(Boolean)
    notes = Column(String)
    tags = relationship('Tags', secondary='twitter_users_tags')

    @hybrid_property
    def friends_followers_ratio(self):
        return round(self.friends_count / max(self.followers_count, 1), 2)

    @friends_followers_ratio.expression
    def friends_followers_ratio(cls):
        return func.round(cls.friends_count / func.max(cls.followers_count), 2)

    blocked_by = Column(Boolean)
    blocking = Column(Boolean)
    contributors_enabled = Column(Boolean)
    created_at = Column(DateTime)
    default_profile = Column(Boolean)
    default_profile_image = Column(Boolean)
    description = Column(String)
    entities = Column(JSONB)
    favourites_count = Column(BIGINT)
    follow_request_sent = Column(Boolean)
    followers_count = Column(BIGINT)
    following = Column(Boolean)
    friends_count = Column(BIGINT)
    geo_enabled = Column(Boolean)
    has_extended_profile = Column(Boolean)
    id = Column(BIGINT, primary_key=True)
    id_str = Column(String)
    is_translation_enabled = Column(Boolean)
    is_translator = Column(Boolean)
    lang = Column(String)
    listed_count = Column(BIGINT)
    live_following = Column(Boolean)
    location = Column(String)
    muting = Column(Boolean)
    name = Column(String)
    notifications = Column(Boolean)
    profile_background_color = Column(String)
    profile_background_image_url = Column(String)
    profile_background_image_url_https = Column(String)
    profile_background_tile = Column(Boolean)
    profile_banner_url = Column(String)
    profile_image_url = Column(String)
    profile_image_url_https = Column(String)
    profile_link_color = Column(String)
    profile_sidebar_border_color = Column(String)
    profile_sidebar_fill_color = Column(String)
    profile_text_color = Column(String)
    profile_use_background_image = Column(Boolean)
    protected = Column(Boolean)
    screen_name = Column(String)
    status = Column(JSONB)
    statuses_count = Column(BIGINT)
    time_zone = Column(String)
    translator_type = Column(String)
    url = Column(String)
    utc_offset = Column(BIGINT)
    verified = Column(Boolean)
