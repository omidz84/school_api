import subprocess

from rest_framework.test import APITestCase
from rest_framework import status

from school import models


class SchoolTest(APITestCase):
    def setUp(self):
        self.valid_data_school = {
            'name': 'مدرسه امید',
            'address': 'یزد',
            'location': '{"type": "point", "coordinates": [10.0, 11.2]}'
        }
        self.invalid_data_school = {
            'address': 'یزد',
            'location': 'hasan'
        }

    def test_create_school_valid(self):
        response = self.client.post('/api/school/', self.valid_data_school)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_school_invalid(self):
        response = self.client.post('/api/school/', self.invalid_data_school)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_school_valid(self):
        response = self.client.get('/api/school/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_school_valid(self):
        models.School.objects.create(
            id=1,
            name='مدرسه',
            address='ایران',
            location='{"type": "point", "coordinates": [10.0, 11.2]}'
        )
        response = self.client.get('/api/school/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_school_invalid(self):
        response = self.client.get('/api/school/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_detail_put_school_valid(self):
        models.School.objects.create(
            id=1,
            name='مدرسه',
            address='ایران',
            location='{"type": "point", "coordinates": [10.0, 11.2]}'
        )
        response = self.client.put('/api/school/1/', self.valid_data_school)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CourseTest(APITestCase):
    def setUp(self):
        self.valid_data_course = {
            'name': 'ریاضی'
        }
        self.invalid_data_course = {
            'name': ''
        }

    def test_create_course_valid(self):
        response = self.client.post('/api/school/course/', self.valid_data_course)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_course_invalid(self):
        response = self.client.post('/api/school/course/', self.invalid_data_course)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_course_valid(self):
        response = self.client.get('/api/school/course/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_course_valid(self):
        models.Course.objects.create(
            id=1,
            name='فیزیک',
        )
        response = self.client.get('/api/school/course/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_get_course_invalid(self):
        response = self.client.get('/api/school/course/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_detail_put_course_valid(self):
        models.Course.objects.create(
            id=1,
            name='فیزیک',
        )
        response = self.client.put('/api/school/course/1/', self.valid_data_course)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


