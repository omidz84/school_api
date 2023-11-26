from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User
from user.serializers import UserLoginSerializer


class UserTest(APITestCase):

    def setUp(self):
        User.objects.create(
            first_name='omid',
            last_name='zare',
            username='omid123',
            password='12345678',
            phone_number='09140695029',
            code_meli='4421365684',
        )
        self.valid_data = {
            'username': 'omid123',
            'password': '12345678'
        }
        self.invalid_password = {
            'username': 'omid123',
            'password': '1234567'
        }

        self.invalid_username = {
            'username': 'hasan',
            'password': '12345678'
        }

    def test_user_login_valid(self):
        response = self.client.post('/api/user/login/', self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_password(self):
        response = self.client.post('/api/user/login/', self.invalid_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_invalid_username(self):
        response = self.client.post('/api/user/login/', self.invalid_username)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_logout_valid(self):
        serializer = UserLoginSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        token = serializer.data['token']['refresh']
        response = self.client.post('/api/user/logout/', {'refresh': token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_logout_invalid(self):
        response = self.client.post('/api/user/logout/', {'refresh': 'toeknmamadhasan'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh_token_valid(self):
        serializer = UserLoginSerializer(data=self.valid_data)
        serializer.is_valid(raise_exception=True)
        token = serializer.data['token']['refresh']
        response = self.client.post('/api/user/token/refresh/', {'refresh': token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token_invalid(self):
        response = self.client.post('/api/user/token/refresh/', {'refresh': 'toeknmamadhasan'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
