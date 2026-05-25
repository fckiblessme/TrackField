from bottle import post, request, redirect as bottle_redirect
import json
import os
from datetime import datetime
from urllib.parse import quote
from competitions_form_validators import (
    validate_author,
    validate_comp_name,
    validate_description,
    validate_phone,
    validate_date
)
# функция загрузки
def load_competitions():
    filepath = 'static/content/data/competitions.json'
    if os.path.exists(filepath):
        try:
            f = open(filepath, 'r', encoding='utf-8')
            competitions = json.load(f)
            f.close() 
        except:
            return []
    else:
        return []
    
    if not competitions:
        return []
    
    # определение текущей даты
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # разделение на будущие и прошедшие
    future = []
    past = []
    
    for comp in competitions:
        try:
            event_date = datetime.strptime(comp['event_date'], "%Y-%m-%d")
            if event_date >= today:
                future.append(comp)
            else:
                past.append(comp)
        except:
            future.append(comp)
    
    # сортировка будущих дат по возрастанию
    n = len(future)
    for i in range(n):
        for j in range(0, n - i - 1):
            if future[j]['event_date'] > future[j + 1]['event_date']:
                future[j], future[j + 1] = future[j + 1], future[j]
    
    return future + past

# сохранение файла
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
    # получение данных из формы
    author = request.forms.getunicode('author')
    comp_name = request.forms.getunicode('comp_name')
    discipline = request.forms.getunicode('discipline')
    event_date = request.forms.get('event_date')
    description = request.forms.getunicode('description')
    phone = request.forms.getunicode('phone')

    # сохранение данных в полях в случае ошибки
    back_params = "&c_author={0}&c_comp_name={1}&c_discipline={2}&c_event_date={3}&c_description={4}&c_phone={5}".format(
        quote(author or ''), 
        quote(comp_name or ''), 
        quote(discipline or ''), 
        quote(event_date or ''), 
        quote(description or ''), 
        quote(phone or '')
    )

    # проверка на пустые поля
    if not author or not comp_name or not discipline or not event_date or not description or not phone or author.strip() == "" or comp_name.strip() == "" or discipline.strip() == "" or description.strip() == "" or phone.strip() == "":
        return bottle_redirect('/new-competitions?error=' + quote('Все поля должны быть заполнены!') + back_params)

    # проверка автора
    if not validate_author(author):
        return bottle_redirect('/new-competitions?error=' + quote('Имя автора содержит недопустимые символы! Используйте только русские буквы, пробелы и дефисы. Длина: 2-50 символов') + back_params)

    # проверка названия соревнования
    if not validate_comp_name(comp_name):
        return bottle_redirect('/new-competitions?error=' + quote('Название содержит недопустимые символы! Используйте буквы, цифры, пробелы, дефисы и точки. Длина: 3-100 символов. Название не может состоять только из цифр или спецсимволов!') + back_params)

    # проверка даты
    if not validate_date(event_date):
        return bottle_redirect('/new-competitions?error=' + quote('Дата должна быть не ранее сегодняшнего дня и не позднее 5 лет от текущей даты!') + back_params)

    # проверка описания
    if not validate_description(description):
        return bottle_redirect('/new-competitions?error=' + quote('Описание должно содержать от 20 до 1000 символов и не может состоять только из цифр или спецсимволов!') + back_params)

    # проверка телефона
    if not validate_phone(phone):
        return bottle_redirect('/new-competitions?error=' + quote('Неверный формат телефона! Пример: +7 XXX XXX-XX-XX') + back_params)

    
    # защита от дубликатов
    competitions = load_competitions()
    for comp in competitions:
        if (comp['comp_name'].lower() == comp_name.strip().lower() and
            comp['event_date'] == event_date and
            comp['discipline'].lower() == discipline.lower()):
            return bottle_redirect('/new-competitions?error=' + quote('Запись уже существует!') + back_params)

    # создание новой записи
    new_comp = {
        "author": author.strip(),
        "comp_name": comp_name.strip(),
        "discipline": discipline,
        "event_date": event_date,
        "description": description.strip(),
        "phone": phone.strip()
    }

    # добавление новой записи
    competitions.insert(0, new_comp)
    save_competitions(competitions)

    # новая страница
    bottle_redirect('/new-competitions')