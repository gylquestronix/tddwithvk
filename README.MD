## Before You Begin

Before you begin we recommend you read about the basics:

- add later
- add later

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


## test

`docker-compose run  web  python3.9 manage.py test`


## sample screenshots
<img width="464" alt="image" src="https://user-images.githubusercontent.com/115542336/205932913-10a1ae9f-6371-4f21-b692-a4e99133c421.png">
<img width="1205" alt="image" src="https://user-images.githubusercontent.com/115542336/205933199-95c478f2-de2a-4a61-b924-1a477b016a36.png">
<img width="1296" alt="image" src="https://user-images.githubusercontent.com/115542336/205933327-b02ace04-be95-42a6-8965-1d5659b0185e.png">



