from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from voidpaste.models import Paste, Category, Comment

User = get_user_model()


class PasteCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.category = Category.objects.create(name="Test Category")

    def test_create_paste_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            reverse("voidpaste:index"),
            {
                "title": "Test Paste",
                "content": "This is a test paste.",
                "category": self.category.id,
                "delete_choice": "never",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Paste.objects.count(), 1)
        self.assertEqual(Paste.objects.first().user, self.user)

    def test_create_paste_unauthenticated(self):
        response = self.client.post(
            reverse("voidpaste:index"),
            {
                "title": "Test Paste",
                "content": "This is a test paste.",
                "category": self.category.id,
                "delete_choice": "never",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Paste.objects.count(), 1)
        self.assertIsNone(Paste.objects.first().user)


class PasteDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.paste = Paste.objects.create(
            title="Test Paste",
            content="This is a test paste.",
            user=self.user,
            link="testlink",
            delete_choice="never",
        )

    def test_paste_detail_view(self):
        response = self.client.get(
            reverse("voidpaste:paste-detail", kwargs={"link": self.paste.link})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.paste.title)


class ProfileListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def test_profile_list_view(self):
        response = self.client.get(reverse("voidpaste:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pastes found.")


class CommentCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.paste = Paste.objects.create(
            title="Test Paste",
            content="This is a test paste.",
            user=self.user,
            link="testlink",
            delete_choice="never",
        )

    def test_create_comment_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            reverse("voidpaste:add-comment", kwargs={"link": self.paste.link}),
            {"content": "This is a test comment."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().user, self.user)

    def test_create_comment_unauthenticated(self):
        response = self.client.post(
            reverse("voidpaste:add-comment", kwargs={"link": self.paste.link}),
            {"content": "This is a test comment."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 0)
