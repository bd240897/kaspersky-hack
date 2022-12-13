# Web приложение для оценки здоровья домашнего питомца "Tail app"
Проект на хакатон Kaspersky SECUR'IT CUP'22

Команда: **Win+ners**

## Демо:
=
[![Watch the video](./materials/prototype_preview.png)](https://youtu.be/aSgtn1f2SU4;)

## Оглавление
0. [Команда](#Команда)
1. [Задача](#Задача)
2. [Архитектура](#Архитектура)
3. [Описание Backend](#Описание-Backend)
4. [Описание Frontend](#Описание-Frontend)
5. [Развёртывание решения](#Развёртывание-решения)
6. [Описание структуры папок проекта](#Описание-структуры-папок-проекта)
7. [Запуск](#Запуск)

## Команда
1. [Дмитрий Борисов](https://t.me/DmitriiBorisov) - backend/frontend
2. [Максим Кишик](https://t.me/kishikmaxim) - backend
3. [Илья Радомский](https://t.me/Tealdris) - devops
4. [Аня Мархаева](https://t.me/privetobnako) - designer

[:arrow_up:Оглавление](#Оглавление)

## Задача
### Описание задачи
Реализовать детектор заболеваний по фотографии poops для собак.

[:arrow_up:Оглавление](#Оглавление)

## Архитектура
    python 3.8
    backend - django rest framework
    forntend - vue.js
    database - sqlite3/ or PostgeSQL

[:arrow_up:Оглавление](#Оглавление)

## Описание Backend

Backend, реализованный на `Django`, нахоодится в папке `api`.
Ниже представлены возможности нашего API

### документация к API

##### `send photo`
    method: POST
    link: http://127.0.0.1:8000/api/v2/request/photo/quick/
    data-parametrs: file: poop.jpg

[:arrow_up:Оглавление](#Оглавление)

## Описание Frontend

Нами был использован `framefork` `vue.js` для создания приложения.

[:arrow_up:Оглавление](#Оглавление)

## Развёртывание решения

Для удобства запуска приложения на разных платформах был использован `docker`. В папке `frontend` есть `dockerfile` который описывает состояние контейнера. Созданный контейнер будет оптравлен и развернут на удаленном сервере

### 1. Установка Docker (Ubuntu 20.04) 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    sudo apt update
    apt-cache policy docker-ce
    sudo apt install docker-ce
    sudo systemctl status docker // status

### 2. Установка Docker-compose (Ubuntu 20.04)
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru

    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version // status


### 3. Запуск через Docker-compose
https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/

    git clone https://github.com/bd240897/kaspersky-hack
    cd kaspersky-hack/
    docker-compose -f docker-compose.back.yml up --build -d 
    docker-compose -f docker-compose.front-nginx.yml up --build -d 
    
[:arrow_up:Оглавление](#Оглавление)

## Описание структуры папок проекта

Размеченные шаблоны страниц для нашего приложения находятся в папке `templates`.
В задании был использован `bootstrap` framework

- **api** - Файлы для бэкенда (django)
  - api - папка с настройками проекта
  - ...
  - pet - приложение с логикой
  - filter - приложение с фильтром входной картиной is_this_poop? 
  - predictor - набор нейронок для предсказания болезней parasites & blood 
    - ...
  - example_data - тестовые данные для БД
- **frontend** - Файлы для фронтенда (vue)
  - public - Общедоступные файлы
  - src - исходники
- **html_templates** - сверстанные шаблоны
- **materials** - дополнительные материалы
- **cnn_learning** - скрипты обучения нейронки

[:arrow_up:Оглавление](#Оглавление)

## Запуск
Протестировать уже запущенный сайт можно по ссылке:</br>

    http://84.201.135.220// (доступен на момент предоставления решения)
    # или
    http://localhost:8080/ (доступен при создании локального проекта)

Админы у админки джанги:
- Логин: "amid", Пароль: "1"

Пользователи:
- Логин: "user1", Пароль: "1234qwerS+"

[:arrow_up:Оглавление](#Оглавление)

## Заметки
```
Оформление гитхаба
https://github.com/GnuriaN/format-README#Оглавление
```
