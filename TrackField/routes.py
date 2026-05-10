from datetime import datetime 
import bottle
from bottle import route, template


def render(tpl_name, **kwargs):
    kwargs['year'] = datetime.now().year
    return template(tpl_name, **kwargs)

@route('/')
def index():
    """Главная страница"""
    return render('index', title='Главная')

@route('/about')
def about():
    """Страница 'О нас'"""
    return render('about', title='О нас')

@route('/sports')
def sports():
    """Страница 'Виды спорта'"""
    # Данные для карточек видов спорта
    sports_data = [
        {
            'name': 'Бег',
            'description': 'Спринт, средние дистанции, марафон, барьерный бег',
            'details': 'Королевская дисциплина легкой атлетики'
        },
        {
            'name': 'Прыжки',
            'description': 'В высоту, с шестом, в длину, тройной прыжок',
            'details': 'Технически сложные виды'
        },
        {
            'name': 'Метания',
            'description': 'Копье, диск, молот, толкание ядра',
            'details': 'Требуют силы и координации',
        },
        {
            'name': 'Многоборье',
            'description': 'Десятиборье, семиборье, пятиборье',
            'details': 'Комплексные соревнования'
        }
    ]
    return render('sports', title='Виды спорта', sports=sports_data)

@route('/competitions')
def competitions():
    """Страница 'Соревнования'"""
    # Данные о соревнованиях
    events = [
        {
            'name': 'Чемпионат мира',
            'date': '15-24 августа 2026',
            'location': 'Токио, Япония',
            'status': 'предстоящее'
        },
        {
            'name': 'Чемпионат Европы',
            'date': '7-12 июня 2026',
            'location': 'Париж, Франция',
            'status': 'предстоящее'
        },
        {
            'name': 'Национальный Чемпионат',
            'date': '3-5 февраля 2026',
            'location': 'Москва, Россия',
            'status': 'завершено',
            'results': 'Результаты'
        },
        {
            'name': 'Зимний кубок',
            'date': '20-22 января 2026',
            'location': 'Санкт-Петербург',
            'status': 'завершено',
            'results': 'Результаты'
        }
    ]
    return render('competitions', title='Соревнования', events=events)

@route('/contact')
def contact():
    """Страница 'Контакты'"""
    return render('contact', title='Контакты')

@route('/news')
def news():
    """Страница 'Новости'"""
    news_items = [
        {
            'title': 'Новый рекорд мира в беге на 100м',
            'date': '25 февраля 2026',
            'preview': 'Легендарный спринтер показал невероятный результат...'
        },
        {
            'title': 'Подготовка к Олимпийским играм',
            'date': '20 февраля 2026',
            'preview': 'Сборная Франции начинает подготовку к главному старту четырехлетия...'
        }
    ]
    return render('news', title="Новости", news=news_items)

# Маршруты для дисциплин
@route('/race-walking')
def race_walking():
    """Страница 'Спортивная ходьба'"""
    return render('race_walking', title='Спортивная ходьба')

@route('/high-jump')
def high_jump():
    """Страница 'Прыжки в высоту'"""
    return render('high_jump', title='Прыжки в высоту')

@route('/run')
def run():
    """Страница 'Бег'"""
    return render('run', title='Бег')

@route('/jump')
def jump():
    """Страница 'Прыжки в длину'"""
    return render('jump', title='Прыжки в длину')

@route('/relay')
def relay():
    """Страница 'Эстафеты'"""
    return render('relay', title='Эстафеты')


@route('/pole-vault')
def pole_vault():
    """Страница 'Прыжки с шестом'"""
    return render('pole_vault', title='Прыжки с шестом')

@route('/shot-put')
def shot_put():
    """Страница 'Толкание ядра'"""
    return render('shot_put', title='Толкание ядра')

@route('/new-competitions')
def new_competitions():
    """Страница 'Соревнования'"""
    from competitions_form import load_competitions
    from bottle import request
    from datetime import datetime
    competitions_list = load_competitions()
    today = datetime.now().strftime("%Y-%m-%d")
    error = request.query.error or ''
    return template('new_competitions', 
        title='Соревнования',
        year=datetime.now().year,
        competitions=competitions_list, 
        today=today,
        error=error,
        c_author=request.query.c_author or '',
        c_comp_name=request.query.c_comp_name or '',
        c_discipline=request.query.c_discipline or '',
        c_event_date=request.query.c_event_date or '',
        c_description=request.query.c_description or '',
        c_phone=request.query.c_phone or ''
    ) 

@route('/partners')
def partners():
    """Страница Партнеры"""
    from partners_form import load_partners
    from bottle import request
    
    partners_list = load_partners()
    error = request.query.error or ''

    p_name = request.query.p_name or ''
    p_desc = request.query.p_desc or ''
    p_phone = request.query.p_phone or ''
    p_date = request.query.p_date or ''

    return render('partners', 
                  title='Партнеры', 
                  partners=partners_list, 
                  error=error,
                  p_name=p_name,
                  p_desc=p_desc,
                  p_phone=p_phone,
                  p_date=p_date)


from bottle import post, request, redirect as bottle_redirect
import re
import json
import os
from datetime import datetime
from urllib.parse import quote

