#!/bin/bash

# Remove db.sqlite3 if exists
if [ -f db.sqlite3 ]; then
    rm db.sqlite3
fi

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
