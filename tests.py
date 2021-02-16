import requests
import unittest


class TestStringMethods(unittest.TestCase):
    def test_request(self): 
        resp_status = requests.get('https://www.trendyol.com/kadin-gunluk-ayakkabi-x-g1-c1352').status_code             
        self.assertEqual(resp_status, 200)

if __name__ == '__main__':
    unittest.main()