# Web приложение для оценки здоровья домашнего питомца "Tail app"
Проект на хакатон Kaspersky SECUR'IT CUP'22

Команда: **Win+ners**

## Демо:
:point_up_2: Clickable :point_up_2:

[![Тут текст](https://drive.google.com/thumbnail?id=1iIsLfswMvU-DMyhAdflM3a4SSJSh7kl8)](https://drive.google.com/file/d/18PhMVwFXAD9kM6L-CI3JkRsXEP9D4qtu/view?usp=share_link)

## Оглавление
0. [Команда](#Команда)
1. [Задача](#Задача)
2. [Архитектура](#Архитектура)
3. [Описание решения](#Описание-решения)
4. [Описание Backend](#Описание-Backend)
5. [Описание Frontend](#Описание-Frontend)
6. [Развёртывание решения](#Развёртывание-решения)
7. [Описание структуры папок проекта](#Описание-структуры-папок-проекта)
8. [Запуск](#Запуск)

## Команда
1. [Дмитрий Борисов](https://t.me/DmitriiBorisov) - backend/frontend
2. [Максим Кишик](https://t.me/kishikmaxim) - backend
3. [Илья Радомский](https://t.me/Tealdris) - devops
4. [Аня Мархаева](https://t.me/privetobnako) - designer

[:arrow_up:Оглавление](#Оглавление)

## Задача
### Номинация

**Special nomination: Family Care: Pet Care**

### Описание задачи

В разделе «Уход за животными» представленные на рассмотрение товары могут быть связаны как с домашними, так и бездомными питомцами, касаться их безопасности, заботы о здоровье и других актуальных аспектов.

### Описание Решения

Наше решение представляет собой веб приложение, призванное решить проблему по уходу за домашним питомцем, а именно, позволить пользователям быстро определить заболевание питомца по фотографии экскрементов.

[:arrow_up:Оглавление](#Оглавление)

## Архитектура
    python 3.8
    backend - django rest framework
    forntend - vue.js
    database - sqlite3

[:arrow_up:Оглавление](#Оглавление)

## Описание Backend

Backend, реализованный на `Django`, нахоодится в папке `api`.
Ниже представлены возможности нашего API

### документация к API

##### `create user`
    method: POST
    link: http://127.0.0.1:8000/api/v1/auth/users/
    data-parametrs: username password

##### `login`
    method: POST
    link: http://127.0.0.1:8000/auth/token/login/
    data-parametrs: username password

##### `user list`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/

##### `logout`
    method: POST
    link: http://127.0.0.1:8000/auth/token/logout/

##### `user infos`
    method: GET
    link: http://127.0.0.1:8000/api/v1/auth/users/me/

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
    docker-compose -f docker-compose.yml up --build

[:arrow_up:Оглавление](#Оглавление)

## Описание структуры папок проекта

Размеченные шаблоны страниц для нашего приложения находятся в папке `templates`.
В задании был использован `bootstrap` framefork

- **api** - Файлы для бэкенда
  - api - папка с настройками проекта
  - ...
  - core - приложение с логикой банка
    - currency - функции для получения курсов валют
    - ...
  - example_data - тестовы данные для БД
- **frontend** - Файлы для фронтенда
  - public - Общедоступные файлы
  - src - исходники
- **html_templates** - сверстанные шаблоны
- **materials** - Видео работы и дополнительные материала

[:arrow_up:Оглавление](#Оглавление)

## Запуск
Протестировать уже запущенный сайт можно по ссылке:

    http://win-plus-ners.ru/ (доступен на момент предоставления решения)
    # или
    http://localhost:8080/ (доступен при создании локального проекта)

Админы:
- Логин: "amid", Пароль: "1"

Пользователи:
- Логин: "user1", Пароль: "1234qwerS+"

[:arrow_up:Оглавление](#Оглавление)

