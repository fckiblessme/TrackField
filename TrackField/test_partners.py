import unittest
import re
from datetime import datetime

def validate_phone(phone: str) -> bool:
    """Проверяет телефон в формате 7XXXXXXXXXX"""
    if not phone:
        return False
    cleaned = re.sub(r'\D', '', phone)
    pattern = r'^7\d{10}$'
    return bool(re.match(pattern, cleaned))

def validate_date_ru(date_str: str) -> bool:
    """
    Проверяет дату в формате ДД-ММ-ГГГГ 
    """
    if not date_str:
        return False
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_date_iso(date_str: str) -> bool:
    """Проверяет дату в формате YYYY-MM-DD """
    if not date_str:
        return False
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestPhoneValidation(unittest.TestCase):

    def test_valid_phone_plain(self):
        self.assertTrue(validate_phone("79991234567"))
    
    def test_valid_phone_formatted(self):
        self.assertTrue(validate_phone("7 999 123-45-67"))
    
    def test_valid_phone_with_plus(self):
        self.assertTrue(validate_phone("+79991234567"))
    
    def test_valid_phone_with_brackets(self):
        self.assertTrue(validate_phone("7(999)1234567"))
    
    def test_invalid_phone_starts_with_8(self):
        self.assertFalse(validate_phone("89991234567"))
    
    def test_invalid_phone_too_short(self):
        self.assertFalse(validate_phone("7999123456"))
    
    def test_invalid_phone_too_long(self):
        self.assertFalse(validate_phone("799912345678"))
    
    def test_invalid_phone_with_letters(self):
        self.assertFalse(validate_phone("7abc1234567"))
    
    def test_empty_phone(self):
        self.assertFalse(validate_phone(""))
    
    def test_none_phone(self):
        self.assertFalse(validate_phone(None))

class TestDateRussian(unittest.TestCase):
    """Тесты для формата ДД-ММ-ГГГГ """
    def test_valid_date(self):
        self.assertTrue(validate_date_ru("15-12-2025"))

    def test_invalid_date_format_slash(self):
        self.assertFalse(validate_date_ru("15/12/2025"))

    def test_invalid_date_order(self):
  
        self.assertFalse(validate_date_ru("2025-12-15"))

    def test_valid_leap_year(self):
        self.assertTrue(validate_date_ru("29-02-2024"))

    def test_invalid_feb29_non_leap(self):
        self.assertFalse(validate_date_ru("29-02-2023"))

    def test_empty_date(self):
        self.assertFalse(validate_date_ru(""))

    def test_invalid_day(self):
        self.assertFalse(validate_date_ru("32-01-2025"))

    def test_invalid_month(self):
        self.assertFalse(validate_date_ru("15-13-2025"))

class TestDateISO(unittest.TestCase):
    def test_valid_iso_date(self):
        self.assertTrue(validate_date_iso("2025-12-15"))

    def test_invalid_iso_date(self):
        self.assertFalse(validate_date_iso("15-12-2025"))


if __name__ == '__main__':
    unittest.main()