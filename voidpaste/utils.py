import random
import string

from django.utils import timezone

DELETE_CHOICES = [
    ("10_minutes", "10 Minutes"),
    ("1_hour", "1 Hour"),
    ("1_day", "1 Day"),
    ("1_week", "1 Week"),
    ("2_weeks", "2 Weeks"),
    ("never", "Never"),
]


def set_delete_time(choice):
    if choice == "10_minutes":
        return timezone.now() + timezone.timedelta(minutes=10)
    elif choice == "1_hour":
        return timezone.now() + timezone.timedelta(hours=1)
    elif choice == "1_day":
        return timezone.now() + timezone.timedelta(days=1)
    elif choice == "1_week":
        return timezone.now() + timezone.timedelta(weeks=1)
    elif choice == "2_weeks":
        return timezone.now() + timezone.timedelta(weeks=2)
    else:
        return None


def generate_unique_link():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))
