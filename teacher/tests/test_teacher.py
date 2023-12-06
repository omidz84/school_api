from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse
from model_bakery import baker

from user.models import User
from check_system_init.utils import group_student, group_teacher


class TeacherRegisterTest(APITestCase):
    def setUp(self):

        group_student()
        group_teacher()

    def test_teacher_register_success(self):
        url = reverse('teacher:register')
        data = {
            'first_name': 'omid',
            'last_name': 'hasani',
            'username': 'omid123',
            'phone_number': '09140695029',
            'code_meli': '4425689143',
            'password': '123456789',
            'password2': '123456789',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(User.objects.count(), 1)

    def test_teacher_register_null(self):
        url = reverse('teacher:register')
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_teacher_register_invalid_phone_number(self):
        url = reverse('teacher:register')
        data = {
            'first_name': 'omid',
            'last_name': 'hasani',
            'username': 'omid123',
            'phone_number': '0913ht8',
            'code_meli': '4425689143',
            'password': '123456789',
            'password2': '123456789',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
