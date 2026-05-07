import bottle
from bottle import (route, run, template, 
static_file, request, redirect)
import os
import sys

# Подключаем маршруты из отдельного файла
import routes

# Раздача статических файлов (CSS, JS, картинки)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

# Обработка 404 ошибки (страница не найдена)
@route('/<:re:.*>')
def not_found(error):
    return template('404', title='Страница не найдена')

@route('/partners')
def partners_page():
    return template('partners', partners=load_partners(), errors={}, values={})

@route('/partners', method='POST')
def add_partner():
    name = request.forms.get('name').strip()
    description = request.forms.get('description').strip()
    phone = request.forms.get('phone').strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    errors = {}
    # Валидация
    if not name: errors['name'] = "Введите наименование компании"
    if len(description) < 10: errors['description'] = "Описание слишком короткое"
    if not re.match(r'^\+7\d{10}$', phone):
        errors['phone'] = "Формат телефона: +79991234567"

    if errors:
        return template('partners', partners=load_partners(), errors=errors, 
                        values={'name': name, 'description': description, 'phone': phone})

    save_partner({'name': name, 'description': description, 'phone': phone, 'date': date})
    return redirect('/partners')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/css')

# Запуск сервера
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='localhost', port=port, debug=True, reloader=True)