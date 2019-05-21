#!/bin/bash

rm -rf ./venv;
virtualenv -p python3 ./venv;

. ./venv/bin/activate;
pip install -r requirements-dev.txt;

pip uninstall sqlparse;
pip install sqlparse==0.2.4;

pip install -r requirements-dev.txt;

python manage.py migrate;
python manage.py makemigrations;
python manage.py makemigrations index;
python manage.py migrate;
python manage.py runserver;
