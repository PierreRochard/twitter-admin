FROM python:alpine

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 zsh linux-headers postgresql-dev && \
    pip3 install --upgrade pip setuptools uWSGI

WORKDIR website

COPY ./requirements.txt .
COPY ./.env .

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN pip3 install --upgrade --no-cache-dir pip -r requirements.txt

CMD [ "uwsgi", "--ini", "app.ini" ]
