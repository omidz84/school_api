from django.contrib.auth.models import Group, Permission


def group_student():
    g_student, x = Group.objects.get_or_create(name='دانش‌ آموز')

    permissions_list = [
        'view_practiceresponse', 'delete_practiceresponse', 'change_practiceresponse', 'add_practiceresponse',
        'view_school', 'view_practice', 'view_news', 'view_course', 'view_class',
    ]
    permissions = Permission.objects.filter(codename__in=permissions_list)
    g_student.permissions.set(permissions)


def group_teacher():
    g_student, x = Group.objects.get_or_create(name='معلم')

    permissions_list = [
        'view_practiceresponse', 'view_school', 'delete_school', 'change_school',
        'add_school', 'view_practice', 'delete_practice', 'change_practice',
        'add_practice', 'view_news', 'delete_news', 'change_news',
        'add_news', 'view_course', 'delete_course', 'change_course',
        'add_course', 'view_class', 'delete_class', 'change_class',
        'add_class',
    ]
    permissions = Permission.objects.filter(codename__in=permissions_list)
    g_student.permissions.set(permissions)
