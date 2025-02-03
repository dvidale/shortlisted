# using python 3.9.18-alpine3.18 as base image
FROM python:3.9.18-alpine3.18 

# installs build-base via Alpine package manager for compiling python packages
RUN apk add build-base

# installs postgresql-dev, gcc, python3-dev, musl-dev via Alpine package manager for compiling psycopg2
RUN apk add postgresql-dev gcc python3-dev musl-dev

#declares variables for build arguments for use running the docker build command 
ARG FLASK_APP
ARG FLASK_ENV
ARG DATABASE_URL
ARG SCHEMA
ARG SECRET_KEY


WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install psycopg2

COPY . .

RUN flask db upgrade
RUN flask seed all
CMD gunicorn app:app