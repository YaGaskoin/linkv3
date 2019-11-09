FROM python:3.6.9-alpine3.10


RUN apk add python3 && mkdir usr/backend
RUN apk add gcc musl-dev python3-dev postgresql-dev &&\
    pip3 install --upgrade pip setuptools pipenv

ADD Pipfile /usr/backend
ADD Pipfile.lock /usr/backend


RUN cd /usr/backend && pipenv install --system --verbose

COPY . /usr/backend

