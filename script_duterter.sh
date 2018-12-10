#!/bin/bash
brew install python;
brew install virtualenv;
git clone https://github.com/nbeny/PortFolio;
cd Portfolio;
rm -rf venv/;
virtualenv -p python3.7 venv;
source ./venv/bin/activate;
cd PortFolio;
pip3 install -r requirements.txt;
python manage.py runserver;