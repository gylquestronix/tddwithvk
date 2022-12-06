## Before You Begin

Before you begin we recommend you read about the basics:

- a
- b

## Prerequisites

Make sure you have installed all of the following prerequisites on your development machine:

- Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
- Docker - link later
- Docker-compose - link later

## Cloning The GitHub Repository

git install https://github.com/repo/repo.git

## install docker and docker-compose

first creates a writeable container layer over the specified image, and then starts it using the specified command.

`docker-compose run web django-admin startproject desiredprojectname .`

# create build and up

`docker-compose up --build`

PS: change the ALLOWED_HOSTS in settings.py

## migrate database

`docker-compose run web python3.9 manage.py migrate`

## create admin account

`docker-compose run web python3.9 manage.py createsuperuser`

## install dep

`docker-compose run web pip install name-to-be-installed`

## start app

`docker-compose run web python3.9 manage.py startapp base`

## make migrations

`docker-compose run  web  python3.9 manage.py makemigrations`

## apply migrations

`docker-compose run  web  python3.9 manage.py migrate`

## shell command

`docker-compose run  web  python3.9 manage.py shell`
