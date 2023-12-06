from django.core.management import call_command
from rest_framework.test import APITestCase
from rest_framework import status

from school import models
from teacher.serializers import TeacherRegisterSerializer
from student.serializers import StudentRegisterSerializer


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


class ClassTest(APITestCase):
    def setUp(self):
        call_command('checksysteminit')
        teacher = TeacherRegisterSerializer(data={
            'first_name': 'omid',
            'last_name': 'zare',
            'username': 'omid123',
            'phone_number': '09140695029',
            'code_meli': '4426598453',
            'password': '123456789',
            'password2': '123456789',
        })
        teacher.is_valid()
        teacher.save()
        student = StudentRegisterSerializer(data={
            'first_name': 'hasan',
            'last_name': 'hasani',
            'username': 'hasan123',
            'phone_number': '09132226985',
            'code_meli': '44165759',
            'password': '123456789',
            'password2': '123456789',
        })
        student.is_valid()
        student.save()
        course = models.Course.objects.create(
            id=1,
            name='فیزیک',
        )
        school = models.School.objects.create(
            id=1,
            name='مدرسه',
            address='ایران',
            location='{"type": "point", "coordinates": [10.0, 11.2]}'
        )
        self.valid_data_class = {
            'school': school.pk,
            'course': course.pk,
            'teacher': teacher.data['id'],
            'students': student.data['id'],
        }
        self.invalid_data_class = {
            'school': 4,
            'course': 2,
            'teacher': 7,
            'students': 6,
        }

    def test_create_course_valid(self):
        response = self.client.post('/api/school/class/', self.valid_data_class)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_course_invalid(self):
        response = self.client.post('/api/school/class/', self.invalid_data_class)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
