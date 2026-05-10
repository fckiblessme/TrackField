import sys
import os
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import unittest
from competitions_form_validators import (
    validate_author,
    validate_comp_name,
    validate_description,
    validate_phone,
    validate_date
)

# тестирование автора
class TestValidateAuthor(unittest.TestCase):


    def test_T_author(self):
        list_T = [
            "Дарья",
            "Дарья Скрыпникова",
            "Анна-Мария",
        ]
        for author in list_T:
            self.assertTrue(validate_author(author))

    def test_F_author(self):
        list_F = [
            "",                 
            "Д",          
            "Darya",      
            "Дарья123",   
            "Д@рья",      
            "....",       
            "12345"       
        ]
        for author in list_F:
            self.assertFalse(validate_author(author))

# тестирование названия
class TestValidateCompName(unittest.TestCase):

    def test_T_comp_name(self):
        list_T = [
            "Чемпионат России",
            "Russian Championship",
            "Чемпионат России 2026",
            "Московский марафон-2025"
        ]
        for name in list_T:
            self.assertTrue(validate_comp_name(name))

    def test_F_comp_name(self):
        list_F = [
            "",                                
            "ЧМ",                  
            "12345",               
            ".........",           
            "A" * 500              
        ]
        for name in list_F:
            self.assertFalse(validate_comp_name(name))

# тестирование описания
class TestValidateDescription(unittest.TestCase):

    def test_T_description(self):
        list_T = [
            "Чемпионат России по лёгкой атлетике в Казани",
            "Соревнования по бегу на дистанцию 100 метров",
            "Открытый чемпионат города по прыжкам в высоту"
        ]
        for desc in list_T:
            self.assertTrue(validate_description(desc))

    def test_F_description(self):
        list_F = [
            "",                                                
            "Чемпионат",                             
            "12345678901234567890",                  
            "@#$%^&*()!@#$%^&*()",                   
            "A" * 2000                              
        ]
        for desc in list_F:
            self.assertFalse(validate_description(desc))

# тестирование телефона
class TestValidatePhone(unittest.TestCase):

    def test_T_phone(self):
        list_T = [
            "+7 964 348-47-12",
            "+7 921 561-45-87",
            "+7 965 163-28-35"
        ]
        for phone in list_T:
            self.assertTrue(validate_phone(phone))

    def test_F_phone(self):
        list_F = [
            "",                                         
            "7 (964) 348-47-12",      
            "+7964348-47-12",       
            "79643484712",            
            "+7 964 348-471",       
            "+7 qwe tyu-io-kj",     
            "+7 964 348--47--123",   
            "+7 (964) 348-47-12",
            "+7 964   348-47-12",
            "+    7 964 348-47-12",
            "+7 964 3484712",
            "+7 964 348 47 12",
            "+7 964 348-47-1",
            "+7 964 348-47-123"
        ]
        for phone in list_F:
            self.assertFalse(validate_phone(phone))

# тестирование даты
class TestValidateDate(unittest.TestCase):

    def test_T_date(self):
        list_T = [
            datetime.now().strftime("%Y-%m-%d"),                    
            (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        ]
        for date in list_T:
            self.assertTrue(validate_date(date))

    def test_F_date(self):
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        list_F = [
            "2020-01-01",          
            yesterday             
        ]
        for date in list_F:
            self.assertFalse(validate_date(date))




if __name__ == '__main__':
    unittest.main()