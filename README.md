# API для базы данных YaMDb

## 1. [Описание](#1)
## 2. [Команды для запуска](#2)
## 3. [Техническая информация](#3)
## 4. [Команда разработки](#4)

---
## 1. Описание <a id=1></a>

Проект предназначен для взаимодействия с API социальной сети YaMDb.
YaMDb собирает отзывы пользователей на различные произведения.

API предоставляет возможность взаимодействовать с базой данных по следующим направлениям:
  - авторизироваться
  - создавать свои отзывы и управлять ими (корректировать\удалять)
  - просматривать и комментировать отзывы других пользователей
  - просматривать комментарии к своему и другим отзывам
  - просматривать произведения, категории и жанры произведений

Перечень запросов к ресурсу можно посмотреть в описании API после настройки и запуска проекта
http://127.0.0.1:8000/redoc/

---
## 2. Команды для запуска <a id=2></a>

Перед запуском необходимо клонировать репозиторий и перейти в него в командной строке.

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Выполнить миграции:
```bash
python3 manage.py migrate
```

Запустить проект:
```bash
python3 manage.py runserver
```

Теперь доступность проекта можно проверить по адресу [http://localhost/admin/](http://localhost/admin/)

---
## 3. Техническая информация <a id=3></a>

Стек технологий:
- Python 3.10
- Django 3.2
- Django Rest
- JWT
---
## 4. Команда разработки <a id=4></a>

- [Павел Воробьёв](https://github.com/PaulSparrowPS)
- [Александр Григорьев](https://github.com/Grigoriev1991)  
- [Антон Дунайкин](https://github.com/Toniccc)
