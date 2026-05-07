from bottle import post, request, redirect as bottle_redirect
import re
import json
import os
from datetime import datetime
from urllib.parse import quote

partners_file = 'static/content/data/partners.json'

def load_partners():
    """Загрузка списка партнеров из JSON файла"""
    if os.path.exists(partners_file):
        try:
            f = open(partners_file, 'r', encoding='utf-8')
            data = json.load(f)
            f.close()
            return data
        except:
            return []
    return []

def save_partners(data):
    """Сохранение списка партнеров в JSON файл"""
    folder = os.path.dirname(partners_file)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    
    try:
        f = open(partners_file, 'w', encoding='utf-8')
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    except:
        print("Ошибка при записи файла партнеров")


@post('/add-partner', method='post')
def add_partner():
    """Добавление нового партнера с валидацией"""
    
    # Получаем данные из формы
    name = request.forms.getunicode('name')
    description = request.forms.getunicode('description')
    join_date = request.forms.get('join_date')
    phone = request.forms.getunicode('phone')

    back_params = "&p_name={0}&p_desc={1}&p_phone={2}&p_date={3}".format(
        quote(name or ''), 
        quote(description or ''), 
        quote(phone or ''), 
        quote(join_date or '')
    )

    # 1. Проверка заполненных полей
    if not name or not description or not join_date or not phone or name.strip() == "" or description.strip() == "":
        error_msg = quote("Все поля должны быть заполнены!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 2. Паттерн для наименования
    name_pattern = r'^[A-Za-zА-Яа-яЁё0-9\s\-\.]{3,100}$'
    if not re.match(name_pattern, name):
        error_msg = quote("Наименование содержит недопустимые символы!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 3. Проверка длины описания
    if len(description) < 20 or len(description) > 1000:
        error_msg = quote("Описание должно содержать от 20 до 1000 символов!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 4. Паттерн для телефона
    phone_pattern = r'^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$'
    if not re.match(phone_pattern, phone):
        error_msg = quote("Неверный формат телефона! Пример: +7 (XXX) XXX-XX-XX")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # Загружаем текущий список
    partners = load_partners()

    # 5. Защита от дубликатов
    for p in partners:
        if p['name'].lower() == name.strip().lower():
            error_msg = quote("Такой партнер уже зарегистрирован!")
            return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # Создание новой записи
    new_partner = {
        "name": name.strip(),
        "description": description.strip(),
        "join_date": join_date,
        "phone": phone.strip(),
        "added_date": datetime.now().strftime("%Y-%m-%d")
    }

    # Добавление в начало списка
    partners.insert(0, new_partner)

    # Сохранение
    save_partners(partners)

    return bottle_redirect('/partners')