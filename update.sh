#!/bin/bash
git pull origin master
python manage.py migrate
