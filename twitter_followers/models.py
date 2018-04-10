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

    is_interesting = Column(Boolean, nullable=True)
    notes = Column(String)
    tags = relationship('Tags', secondary='twitter_users_tags')

    @hybrid_property
    def friends_followers_ratio(self):
        return round(self.friends_count / max(self.followers_count, 1), 2)

    @friends_followers_ratio.expression
    def friends_followers_ratio(cls):
        return func.round(cls.friends_count / func.max(cls.followers_count), 2)

    blocked_by = Column(Boolean, nullable=True)
    blocking = Column(Boolean, nullable=True)
    contributors_enabled = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=True)
    default_profile = Column(Boolean, nullable=True)
    default_profile_image = Column(Boolean, nullable=True)
    description = Column(String, nullable=True)
    entities = Column(JSONB, nullable=True)
    favourites_count = Column(BIGINT, nullable=True)
    follow_request_sent = Column(Boolean, nullable=True)
    followers_count = Column(BIGINT, nullable=True)
    following = Column(Boolean, nullable=True)
    friends_count = Column(BIGINT, nullable=True)
    geo_enabled = Column(Boolean, nullable=True)
    has_extended_profile = Column(Boolean, nullable=True)
    id = Column(BIGINT, primary_key=True)
    id_str = Column(String, nullable=True)
    is_translation_enabled = Column(Boolean, nullable=True)
    is_translator = Column(Boolean, nullable=True)
    lang = Column(String, nullable=True)
    listed_count = Column(BIGINT, nullable=True)
    live_following = Column(Boolean, nullable=True)
    location = Column(String, nullable=True)
    muting = Column(Boolean, nullable=True)
    name = Column(String, nullable=True)
    notifications = Column(Boolean, nullable=True)
    profile_background_color = Column(String, nullable=True)
    profile_background_image_url = Column(String, nullable=True)
    profile_background_image_url_https = Column(String, nullable=True)
    profile_background_tile = Column(Boolean, nullable=True)
    profile_banner_url = Column(String, nullable=True)
    profile_image_url = Column(String, nullable=True)
    profile_image_url_https = Column(String, nullable=True)
    profile_link_color = Column(String, nullable=True)
    profile_sidebar_border_color = Column(String, nullable=True)
    profile_sidebar_fill_color = Column(String, nullable=True)
    profile_text_color = Column(String, nullable=True)
    profile_use_background_image = Column(Boolean, nullable=True)
    protected = Column(Boolean, nullable=True)
    screen_name = Column(String, nullable=True)
    status = Column(JSONB, nullable=True)
    statuses_count = Column(BIGINT, nullable=True)
    time_zone = Column(String, nullable=True)
    translator_type = Column(String, nullable=True)
    url = Column(String, nullable=True)
    utc_offset = Column(BIGINT, nullable=True)
    verified = Column(Boolean, nullable=True)
