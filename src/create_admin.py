import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Render User Creater'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if not username or not password:
            self.stdout.write(self.style.ERROR('ERROR'))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f"'{username}' ALREADY USE."))
            return

        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' CREATED!"))