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
    name_pattern = r'^[A-Za-zА-Яа-яЁё0-9.]{3,100}$'
    if not re.match(name_pattern, name):
        error_msg = quote("Наименование содержит недопустимые символы!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 3. Проверка длины описания
    desc_pattern = r'^[A-Za-zА-Яа-яЁё0-9\s\-\.\,\!\?\:\;\(\)\[\]\"\'\«\»]{20,1000}$'
    if not re.match(desc_pattern, description.strip()):
        error_msg = quote("Описание содержит недопустимые символы!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 4. Паттерн и проверка для телефона
    cleaned_phone = re.sub(r'\D', '', phone)

    phone_pattern = r'^7\d{10}$'
    if not re.match(phone_pattern, cleaned_phone):
        error_msg = quote("Неверный формат телефона! Пример: 7XXXXXXXXXX")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    phone = cleaned_phone

    # 5. Проверка даты 
    current_year = datetime.now().year

    if not join_date:
        error_msg = quote("Не указана дата начала сотрудничества!")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    try:
        dt = datetime.strptime(join_date, '%Y-%m-%d')
    except ValueError:
        error_msg = quote("Неверный формат даты! Используйте YYYY-MM-DD.")
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # Ограничение по году 
    if dt.year < 2020 or dt.year > current_year + 5:
        error_msg = quote("Год должен быть от 2020 до {0}.".format(current_year + 5))
        return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    partners = load_partners()

    # 6. Защита от дубликатов по имени
    for p in partners:
        if p['name'].lower() == name.strip().lower():
            error_msg = quote("Такой партнер уже зарегистрирован!")
            return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # 7. Защита от дубликатов по телефону
    for p in partners:
        if p['phone'] == phone:
            error_msg = quote("Партнёр с таким номером телефона уже существует!")
            return bottle_redirect('/partners?error={0}{1}'.format(error_msg, back_params))

    # Создание новой записи
    new_partner = {
        "name": name.strip(),
        "description": description.strip(),
        "join_date": join_date,        
        "phone": phone,
        "added_date": datetime.now().strftime("%Y-%m-%d")
    }

    # Добавление в начало списка
    partners.insert(0, new_partner)

    # Сохранение
    save_partners(partners)

    return bottle_redirect('/partners')   