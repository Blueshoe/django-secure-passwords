from django.core.management.base import BaseCommand

from securepasswords.models import PasswordProfile


class Command(BaseCommand):
    help = "Enforces password renewal"

    def handle(self, *args, **options):
        PasswordProfile.objects.update(force_change=True)
