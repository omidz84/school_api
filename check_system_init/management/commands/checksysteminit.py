from django.core.management import BaseCommand
from check_system_init.utils import group_student, group_teacher


class Command(BaseCommand):

    def handle(self, *args, **options):
        group_student()
        group_teacher()
