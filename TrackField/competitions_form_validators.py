import re
from datetime import datetime

# проверка имени автора
def validate_author(author):
    pattern = r'^[А-Яа-яЁё\s\-]{3,50}$'
    return re.match(pattern, author) is not None

# проверка названия соревнования
def validate_comp_name(comp_name):
    pattern = r'^[A-Za-zА-Яа-яЁё0-9\s\-\.]{3,100}$'
    if not re.match(pattern, comp_name):
        return False
    if comp_name.isdigit():
        return False
    if not any(char.isalpha() for char in comp_name):
        return False
    return True

# проверка, что дата не раньше сегодняшней
def validate_date(event_date):
    if not event_date:
        return False
    try:
        event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return event_date_obj >= today
    except ValueError:
        return False

# проверка описания
def validate_description(description):
    if len(description) < 20 or len(description) > 1000:
        return False
    if description.isdigit():
        return False
    if not any(char.isalpha() for char in description):
        return False
    return True

# проверка телефона
def validate_phone(phone):
    pattern = r'^\+7\s\d{3}\s\d{3}-\d{2}-\d{2}$'
    return re.match(pattern, phone) is not None

