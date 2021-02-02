from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Enforces password renewal"

    def handle(self, *args, **options):
        # TODO
        pass
