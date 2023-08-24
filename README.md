# Qortex Test Task

## Основные используемые технологии
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)![version](https://img.shields.io/badge/3.11-gray) <br>
![Django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white)![version](https://img.shields.io/badge/4.2.4-gray) <br>
![DjangoREST](https://img.shields.io/badge/DjangoREST-800000.svg?style=flat&logo=Django&logoColor=white)![version](https://img.shields.io/badge/3.14.0-gray)

## Запуск тестового проекта
1. Скачать, установить и включить Docker для вашей системы.
<br> https://www.docker.com
2. Открыть папку с проектом в терминале.
3. Клонировать репозиторий проекта.
```sh
git clone https://github.com/JxSol/xetroq_test.git
```
4. Запустить docker-compose:
```sh
docker compose up -d
```

## Особенности исполнения задания
- Swagger находится на http://localhost
- Статика отключена за ненадобностью.
- Volumes для БД не прокинуты намерено.
- Запуск проекта происходит в debug-режиме.
- Некоторые избыточные фичи вставлены по привычке (например gunicorn в Dockerfile).
