import unittest
import re
from datetime import datetime

def validate_phone(phone: str) -> bool:
    """Проверяет телефон +7 (XXX) XXX-XX-XX"""
    pattern = r'^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$'
    return bool(re.match(pattern, phone))

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
    def test_valid_phone(self):
        self.assertTrue(validate_phone("+7 (999) 123-45-67"))

    def test_invalid_phone_no_plus(self):
        self.assertFalse(validate_phone("7 (999) 123-45-67"))

    def test_invalid_phone_no_brackets(self):
        self.assertFalse(validate_phone("+7 999 123-45-67"))

    def test_invalid_phone_wrong_separator(self):
        self.assertFalse(validate_phone("+7 (999) 123.45.67"))

    def test_empty_phone(self):
        self.assertFalse(validate_phone(""))

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