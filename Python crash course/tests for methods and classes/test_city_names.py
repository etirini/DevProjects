
from city_function import citi_country 
import unittest

class TestCityFunction(unittest.TestCase):
    def test_name_and_country_cont(self):
        formatted_geo = citi_country('aa', 'bb', 'cc')
        self.assertEqual(formatted_geo, 'Aa Bb Cc')
    
 
    def test_name_and_country(self):
        formatted_geo = citi_country('aa', 'bb')
        self.assertEqual(formatted_geo, 'Aa Bb')


if __name__ == '__main__':
    unittest.main()
