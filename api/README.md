# django rest framework
    python 3.8
    django 3.2.11

# Запуск
    pip install -r req.txt

### миграции
    python manage.py migrate
    python manage.py makemigrations core
    python manage.py migrate

### загрузка данных
    python manage.py loaddata example_data/user.json
    python manage.py loaddata example_data/core.json

### загрузка данных
    python manage.py runserver


### superuser 
    username - amid
    password - 1

# URL
    
# один пост по id
    http://127.0.0.1:8000/api/data/?id=1

# список всех постов
    http://127.0.0.1:8000/api/data/list/