from bottle import route, request, redirect, template
import json
import os
import re
from datetime import datetime

DATA_DIR = 'data'
REVIEWS_FILE = os.path.join(DATA_DIR, 'reviews.json')

def load_reviews():
    """Загружает отзывы из файла"""
    if not os.path.exists(REVIEWS_FILE):
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
    """Проверяет дату: формат ГГГГ-ММ-ДД и не в будущем"""
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d')
        today = datetime.now()
        
        if input_date > today:
            return False, "Дата не может быть в будущем"
        
        return True, date_str
    except ValueError:
        return False, "Дата должна быть в формате ГГГГ-ММ-ДД"


@route('/reviews')
def reviews_page():
    """Страница отзывов"""
    reviews = load_reviews()
    reviews.sort(key=lambda x: x.get('date', ''), reverse=True)
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

    
    form_data = {
        'author': author,
        'text': text,
        'date': date,
        'phone': phone
    }
    
    errors = {}
    
    if not author:
        errors['author'] = 'Введите ваше имя'
    elif len(author) < 2:
        errors['author'] = 'Имя должно быть не менее 2 символов'
    elif len(author) > 50:
        errors['author'] = 'Имя не более 50 символов'
    
    if not text:
        errors['text'] = 'Введите текст отзыва'
    elif len(text) < 10:
        errors['text'] = 'Текст должен быть не менее 10 символов'
    elif len(text) > 1000:
        errors['text'] = 'Текст не более 1000 символов'
    
    if not date:
        errors['date'] = 'Выберите дату'
    else:
        date_valid, date_msg = validate_date(date)
        if not date_valid:
            errors['date'] = date_msg
    
    if not phone:
        errors['phone'] = 'Введите номер телефона'
    else:
        phone_valid, phone_msg = validate_phone(phone)
        if not phone_valid:
            errors['phone'] = phone_msg
        else:
            form_data['phone'] = phone_msg
    
    if errors:
        reviews = load_reviews()
        reviews.sort(key=lambda x: x.get('date', ''), reverse=True)
        return template('reviews', 
                       title='Отзывы',
                       reviews=reviews, 
                       form_data=form_data, 
                       errors=errors, year=datetime.now().year)
    
    reviews = load_reviews()
    new_id = 1
    if reviews:
        new_id = max(r.get('id', 0) for r in reviews) + 1
    
    new_review = {
        'id': new_id,
        'author': author,
        'text': text,
        'date': date,
        'phone': form_data['phone']
    }
    
    reviews.append(new_review)
    save_reviews(reviews)
    
    redirect('/reviews')