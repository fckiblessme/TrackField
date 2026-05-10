from bottle import post, request, redirect as bottle_redirect
import re
import json
import os
from datetime import datetime
from urllib.parse import quote


# Функция загрузки
def load_competitions():
    filepath = 'static/content/data/competitions.json'
    if os.path.exists(filepath):
        try:
            f = open(filepath, 'r', encoding='utf-8')
            data = json.load(f)
            f.close() 
            return data
        except:
            return []
    return []

# Функция сохранения
def save_competitions(data):
    filepath = 'static/content/data/competitions.json'
    
    # Создаем папку, если она не существует
    folder = os.path.dirname(filepath)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    
    try:
        f = open(filepath, 'w', encoding='utf-8')
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close() 
    except:
        print("Ошибка при записи файла")


@post('/new-competitions', method='post')
def add_competition():
    author = request.forms.getunicode('author')
    comp_name = request.forms.getunicode('comp_name')
    discipline = request.forms.getunicode('discipline')
    event_date = request.forms.get('event_date')
    description = request.forms.getunicode('description')
    phone = request.forms.getunicode('phone')

    # проверка заполненных полей 
    if not author or not comp_name or not discipline or not event_date or not description or not phone or author.strip() == "" or comp_name.strip() == "" or description.strip() == "":
        return bottle_redirect('/new-competitions?error=' + quote('Все поля должны быть заполнены!'))

    # паттерн для автора
    author_pattern = r'^[А-Яа-яЁё\s\-]{2,50}$'
    if not re.match(author_pattern, author):
        return bottle_redirect('/new-competitions?error=' + quote('Имя автора содержит недопустимые символы!'))

    # паттерн для названия
    comp_name_pattern = r'^[A-Za-zА-Яа-яЁё0-9\s\-\.]{3,100}$'
    if not re.match(comp_name_pattern, comp_name):
        return bottle_redirect('/new-competitions?error=' + quote('Название содержит недопустимые символы!'))
    # проверка названия на содержание буквенных символов
    if comp_name.isdigit():
        return bottle_redirect('/new-competitions?error=' + quote('Название не может состоять исключительно из цифр!'))

    if not any(char.isalpha() for char in comp_name):
        return bottle_redirect('/new-competitions?error=' + quote('Название не может состоять исключительно из специальных символов!'))

 

    # проверка длины описания
    if len(description) < 20 or len(description) > 1000:
        return bottle_redirect('/new-competitions?error=' + quote('Описание должно содержать от 20 до 1000 символов!'))
    # проверка описания на содержание буквенных символов
    if description.isdigit():
        return bottle_redirect('/new-competitions?error=' + quote('Описание не может состоять исключительно из цифр!'))

    if not any(char.isalpha() for char in description):
        return bottle_redirect('/new-competitions?error=' + quote('Описание не может состоять исключительно из специальных символов!'))

    # паттерн для телефона
    if phone and phone.strip():
        phone_pattern = r'^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$'
        if not re.match(phone_pattern, phone):
            return bottle_redirect('/new-competitions?error=' + quote('Неверный формат телефона! Пример: +7 (XXX) XXX-XX-XX'))

    # загрузка существующих соревнований
    competitions = load_competitions()

    # защита от дуБликатов 
    for comp in competitions:
        if (comp['comp_name'].lower() == comp_name.strip().lower() and 
            comp['event_date'] == event_date and 
            comp['discipline'].lower() == discipline.lower()):
            return bottle_redirect('/new-competitions?error=' + quote('Запись уже существует!'))

    # создание новой записи
    new_comp = {
        "author": author.strip(),
        "comp_name": comp_name.strip(),
        "discipline": discipline,
        "event_date": event_date,
        "description": description.strip(),
        "phone": phone.strip() if phone else "",
        "added_date": datetime.now().strftime("%Y-%m-%d")
    }

    # добавление в начало списка 
    competitions.insert(0, new_comp)

    # сохранение
    save_competitions(competitions)

    # перенаправление обратно на страницу
    bottle_redirect('/new-competitions')