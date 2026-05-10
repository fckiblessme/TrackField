import unittest
from datetime import datetime, timedelta
from reviews import validate_phone, validate_date

class TestPhone(unittest.TestCase):
    def test_correct_phones(self):
        correct_list = [
            "+7 (912) 345-67-89",
            "+7 (123) 456-78-90",
            "+7 (999) 888-77-66",
            "+7 (000) 111-22-33"
        ]
        for phone in correct_list:
            with self.subTest(phone=phone):
                self.assertTrue(validate_phone(phone)[0])

    def test_incorrect_phones(self):
        incorrect_list = [
            "",
            "1",
            "912345",
            "9123456789",
            "89123456789",
            "79123456789",
            "912abc6789",
            "+7 912 345-67-89",
            "+7(912)345-67-89",
            "7 (912) 345-67-89",
            "+7 (912) 3456789",
            "+7 (912) 345-67-8"
        ]
        for phone in incorrect_list:
            with self.subTest(phone=phone):
                self.assertFalse(validate_phone(phone)[0])

class TestDate(unittest.TestCase):
    def test_correct_dates(self):
        today = datetime.now().strftime('%Y-%m-%d')
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        last_year = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        
        correct_list = [
            yesterday,
            today,
            last_year,
            "2024-02-29",
            "2023-01-01"
        ]
        for date in correct_list:
            with self.subTest(date=date):
                self.assertTrue(validate_date(date)[0])

    def test_incorrect_dates(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        next_year = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
        
        incorrect_list = [
            "",
            "20.05.2025",
            "2025-13-01",    
            "2025-02-30", 
            "2025-02-29", 
            "25-05-20",
            "2025/05/20",
            "2025-05",
            tomorrow, 
            next_year 
        ]
        for date in incorrect_list:
            with self.subTest(date=date):
                self.assertFalse(validate_date(date)[0])

if __name__ == '__main__':
    unittest.main()