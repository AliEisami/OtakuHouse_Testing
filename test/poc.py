import unittest
import requests


class POC(unittest.TestCase):

    # Registration
    def test_already_registration(self):
        url = 'http://127.0.0.1:8000/api/users/register/'
        payload = {
            "email": "qautomation5tech@gmail.com",
            "name": "5tech",
            "password": "@QAutomation5"
        }
        response = requests.post(url=url, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], 'qautomation5tech@gmail.com')

    # Login
    def test_login(self):
        url = 'http://127.0.0.1:8000/api/users/login/'
        payload = {
            "username": "qautomation5tech@gmail.com",
            "password": "@QAutomation5"
        }
        response = requests.post(url=url, data=payload)
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], 'qautomation5tech@gmail.com')
