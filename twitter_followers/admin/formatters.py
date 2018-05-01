import requests
from markupsafe import Markup
from requests import ReadTimeout


def screen_name_formatter(view, context, model, name):
    return Markup(
        f'<a href="https://twitter.com/{model.screen_name}">{model.screen_name}</a>')


def image_formatter(view, context, model, name):
    url = getattr(model, name)
    return Markup(f'<img src="{url}">')


def url_formatter(view, context, model, name):
    # url = getattr(model, name)
    # if url is not None:
    #     try:
    #         site = requests.get(url, timeout=0.5)
    #     except ReadTimeout:
    #         return None
    #     url = site.url
    #     return Markup(f'<a href="{url}">{url}</a>')
    return None
#