#!/bin/sh

# Выполняем миграции
python manage.py migrate
python manage.py makemigrations core
python manage.py makemigrations pet
python manage.py migrate
# загружаем тестовые данные
python manage.py loaddata database_example/user.json
python manage.py loaddata database_example/core.json
python manage.py loaddata database_example/pet.json


exec "$@"