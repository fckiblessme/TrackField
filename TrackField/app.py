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

# Запуск сервера
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='localhost', port=port, debug=True, reloader=True)