import bottle
from bottle import (route, run, template, 
static_file, request, redirect)
import os
import sys
import reviews

import routes

sys.stdout.reconfigure(encoding='utf-8')


@bottle.error(404)
def error404(error):
    return "<h1>404 Страница не найдена</h1><p>Вернитесь на <a href='/'>главную</a></p>"

# Раздача статики (лучше без точки перед слэшем)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

# # Обработка 404 ошибки (страница не найдена)
# @route('/<:re:.*>')
# def not_found(error):
#     return template('404', title='Страница не найдена')

    return static_file(filepath, root='static')

# Запуск сервера
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='localhost', port=port, debug=True, reloader=True)