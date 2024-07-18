from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import set_delete_time, generate_unique_link, DELETE_CHOICES


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Paste(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    link = models.CharField(max_length=8, unique=True, default=generate_unique_link)
    delete_at = models.DateTimeField(null=True, blank=True)
    delete_choice = models.CharField(
        max_length=10, choices=DELETE_CHOICES, default="never"
    )

    def save(self, *args, **kwargs):
        if not self.link:
            self.link = generate_unique_link()
        if not self.delete_at and self.delete_choice != "never":
            self.delete_at = set_delete_time(self.delete_choice)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    paste = models.ForeignKey(Paste, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.paste.title}"
