from django.core.management.base import BaseCommand
from voidpaste.models import Paste
from django.utils import timezone


class Command(BaseCommand):
    help = 'Delete expired pastes'

    def handle(self, *args, **kwargs):
        expired_pastes = Paste.objects.filter(delete_at__lte=timezone.now())
        count = expired_pastes.count()
        expired_pastes.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} expired pastes.'))
