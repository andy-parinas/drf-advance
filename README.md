# drf-advance

Django Rest Framework Advance Tutorial

## Create a Django Project

docker compose run --rm app sh -c "django-admin startproject app ."

## Create a Django App

docker compose run --rm app sh -c "python manage.py startapp core"

## Lint using Flake8

docker compose run --rm app sh -c "flake8"

## Run Test

docker compose run --rm app sh -c "python manage.py test"

## Run Migration

docker compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
