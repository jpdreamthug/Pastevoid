import random
import string
from datetime import timedelta

from django.utils import timezone

DELETE_CHOICES = [
    ("1_hour", "1 Hour"),
    ("1_day", "1 Day"),
    ("1_week", "1 Week"),
    ("never", "Never"),
]


def set_delete_time(choice):
    if choice == "1_hour":
        return timezone.now() + timedelta(hours=1)
    elif choice == "1_day":
        return timezone.now() + timedelta(days=1)
    elif choice == "1_week":
        return timezone.now() + timedelta(weeks=1)
    else:
        return None


def generate_unique_link():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))
