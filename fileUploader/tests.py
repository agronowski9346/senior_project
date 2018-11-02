from django.test import TestCase
from django.test import Client
from rest_framework import status
import unittest
# Create your tests here.

#tests /register to see a user can register with a PUT request
class Register(TestCase):
    def test_register(self):
        c = Client()
        response = Client().put(
        path = '/register/',
        data = {
            'username': 'taesting',
            'email' : 'testing',
            'first_name' : 'testing',
            'last_name' : 'testing',
            'password' : 'testing',
            'phone_number' : 'testing',
            'home_address' : 'testing',
        },
        content_type = 'application/x-www-form-urlencoded'
        ) 
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

#tests the users API point
class Users(TestCase):
    def test_selecting_users(self):
        c = Client()
        response = c.get('/api/users/')
        self.assertEquals(response.context_data["username"], status.HTTP_201_CREATED)