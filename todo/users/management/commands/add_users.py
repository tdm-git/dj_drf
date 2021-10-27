from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user1 = User.objects.create_user(
            username='test_user1',
            email='test_user1@todo.local',
            first_name='test_user1',
            password='qwerty',)
        user2 = User.objects.create_user(
            username='test_user2',
            email='test_user2@todo.local',
            first_name='test_user2',
            password='qwerty', )
        user3 = User.objects.create_user(
            username='test_user3',
            email='test_user3@todo.local',
            first_name='test_user3',
            password='qwerty', )

