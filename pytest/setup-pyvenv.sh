#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
#pip install --upgrade pip
#pip install beautifulsoup4
#pip install lxml
pip freeze > venv/requirements.txt
deactivate






