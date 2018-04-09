from sqlalchemy import (
    Column,
    DateTime,
    BIGINT,
    String,
    Boolean)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TwitterUsers(Base):
    __tablename__ = 'twitter_users'

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
