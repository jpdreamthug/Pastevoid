from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from voidpaste.models import Paste, Category, Comment
from voidpaste.utils import generate_unique_link

User = get_user_model()


class CategoryModelTest(TestCase):
    def test_string_representation(self):
        category = Category(name="Test Category")
        self.assertEqual(str(category), category.name)


class PasteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.category = Category.objects.create(name="Test Category")
        self.paste = Paste.objects.create(
            title="Test Paste",
            content="This is a test paste.",
            user=self.user,
            category=self.category,
            link=generate_unique_link(),
            delete_choice="never"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.paste), self.paste.title)

    def test_generate_unique_link(self):
        self.assertEqual(len(self.paste.link), 8)
        self.assertTrue(self.paste.link.isalnum())

    def test_set_delete_time(self):
        self.paste.delete_choice = "1_day"
        self.paste.save()
        expected_delete_time = self.paste.created_at + timezone.timedelta(days=1)
        self.assertAlmostEqual(self.paste.delete_at, expected_delete_time, delta=timezone.timedelta(seconds=1))


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.paste = Paste.objects.create(
            title="Test Paste",
            content="This is a test paste.",
            user=self.user,
            link=generate_unique_link(),
            delete_choice="never"
        )
        self.comment = Comment.objects.create(
            content="This is a test comment.",
            paste=self.paste,
            user=self.user
        )

    def test_string_representation(self):
        expected_string = f"Comment by {self.comment.user.username} on {self.comment.paste.title}"
        self.assertEqual(str(self.comment), expected_string)
