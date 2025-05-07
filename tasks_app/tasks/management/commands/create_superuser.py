import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
env_path = settings.BASE_DIR / ".." / ".env"
load_dotenv(env_path)


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=os.getenv('SUPERUSER_ADMIN')).exists():
            User.objects.create_superuser(
                os.getenv('SUPERUSER_ADMIN'),
                os.getenv('SUPERUSER_EMAIL'),
                os.getenv('SUPERUSER_PASSWORD')
            )
            self.stdout.write(self.style.SUCCESS(
                'Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Superuser already exists.'))