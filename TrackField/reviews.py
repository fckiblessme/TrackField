from bottle import route, request, redirect, template
import json
import os
import re
from datetime import datetime

DATA_DIR = 'data'
REVIEWS_FILE = os.path.join(DATA_DIR, 'reviews.json')

def load_reviews():
    """Загружает отзывы из файла"""
    # если файла с отзывами не существует
    if not os.path.exists(REVIEWS_FILE):
        #возвращаем пустой список
        return []
    try:
        with open(REVIEWS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_reviews(reviews):
    """Сохраняет отзывы в файл"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    with open(REVIEWS_FILE, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

def validate_date(date_str):
    """Проверяем дату"""
    try:
        #Преобразуем строку в объект даты
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        #Текущая дата и время
        today = datetime.now()
        
        #Если дата больше текущей
        if input_date > today:
            return False, "Дата не может быть в будущем"
        
        return True, date_str
    except ValueError:
        return False, "Дата должна быть в формате ГГГГ-ММ-ДД"

def validate_phone(phone):
    """Проверка телефона"""
    import re
    pattern = r'^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$'
    
    #Проверка на соответствие шаблону
    if re.match(pattern, phone):
        return True, phone
    else:
        return False, "Телефон должен быть в формате +7 (XXX) XXX-XX-XX"

def validate_name(name):
    """Проверяет имя автора"""
    name = name.strip()
    #Если поле пустое
    if not name:
        return False, "Введите ваше имя"
    #Если имя менее 2 символов
    if len(name) < 2:
        return False, "Имя должно быть не менее 2 символов"
    #Если имя больше 50 символов
    if len(name) > 50:
        return False, "Имя не более 50 символов"
    return True, name

def validate_text(text):
    """Проверяет текст отзыва"""
    text = text.strip()
    #Если поле пустое
    if not text:
        return False, "Введите текст отзыва"
    #Если отзыв меньше 10 символов
    if len(text) < 10:
        return False, "Текст должен быть не менее 10 символов"
    #Если отзыв больше 1000 символов
    if len(text) > 1000:
        return False, "Текст не более 1000 символов"
    return True, text

@route('/reviews')
def reviews_page():
    """Страница отзывов"""
    #Загружаем все отзывы из файла
    reviews = load_reviews()
    #Сортируем по дате
    reviews.sort(key=lambda x: x.get('date', ''), reverse=True)

    #Отображение шаблона
    return template('reviews', 
                   title='Отзывы',
                   reviews=reviews, 
                   form_data={}, 
                   errors={})


@route('/reviews/add', method='POST')
def add_review():
    """Добавление отзыва"""
    author = request.forms.getunicode('author', '').strip()
    text = request.forms.getunicode('text', '').strip()
    date = request.forms.get('date', '').strip()
    phone = request.forms.getunicode('phone', '').strip()
    rating = request.forms.get('rating', '').strip()

    #Сохранение введенных данных при ошибке в поле
    form_data = {
        'author': author,
        'text': text,
        'date': date,
        'phone': phone,
        'rating': rating
    }
    
    errors = {}
    
    #Если поле пустое
    if not author:
        errors['author'] = 'Введите ваше имя'
    #Если имя меньше 2 символов
    elif len(author) < 2:
        errors['author'] = 'Имя должно быть не менее 2 символов'
    #Если имя больше 50 символов
    elif len(author) > 50:
        errors['author'] = 'Имя не более 50 символов'
    
    #Если поле пустое
    if not text:
        errors['text'] = 'Введите текст отзыва'
    #Если текст меньше 10 символов
    elif len(text) < 10:
        errors['text'] = 'Текст должен быть не менее 10 символов'
    #Если текст больше 1000 символов
    elif len(text) > 1000:
        errors['text'] = 'Текст не более 1000 символов'
    
    #Если поле пустое
    if not date:
        errors['date'] = 'Выберите дату'
    else:
        #Вызов функции для проверки
        date_valid, date_msg = validate_date(date)
        #Если дата не прошла проверку
        if not date_valid:
            #Добавление сообщения об ошибкке
            errors['date'] = date_msg
    
    #Если поле пустое
    if not phone:
        errors['phone'] = 'Введите номер телефона'
    else:
        #Вызов функции для проверки
        phone_valid, phone_msg = validate_phone(phone)
        #Если телефон не прошел проверку
        if not phone_valid:
            errors['phone'] = phone_msg
        else:
            form_data['phone'] = phone_msg

    #Если оценка не выбрана
    if not rating:
        errors['rating'] = 'Выберите оценку'
    #Если оценка не является числом
    elif not rating.isdigit():
        errors['rating'] = 'Оценка должна быть числом'
    #Если оценка не от 1 до 5
    elif int(rating) < 1 or int(rating) > 5:
        errors['rating'] = 'Оценка должна быть от 1 до 5'

    #Если словарь не пустой
    if errors:
        #Загрузка существующих отзывов
        reviews = load_reviews()
        #Сортировка по дате
        reviews.sort(key=lambda x: x.get('date', ''), reverse=True)
        #Возврат страницы отзывов
        return template('reviews', 
                       title='Отзывы',
                       reviews=reviews, 
                       form_data=form_data, 
                       errors=errors, year=datetime.now().year)
   
    #Загрузка текущих отзывов
    reviews = load_reviews()
    #Генерация кода отзывов
    new_id = 1
    #Нахождение максимального кода
    if reviews:
        new_id = max(r.get('id', 0) for r in reviews) + 1
    
    #Создание нового отзыва
    new_review = {
        'id': new_id,
        'author': author,
        'text': text,
        'date': date,
        'phone': form_data['phone'],
        'rating': int(rating)
    }
    
    #Добавление нового отзыва в список
    reviews.append(new_review)

    #Сохранение обновленного списка
    save_reviews(reviews)
    
    redirect('/reviews')