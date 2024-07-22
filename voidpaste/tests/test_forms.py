from django.test import TestCase
from voidpaste.forms import PasteForm, CommentForm, CustomUserCreationForm
from voidpaste.models import Category


class PasteFormTest(TestCase):
    def test_valid_form(self):
        category = Category.objects.create(name="Test Category")
        form_data = {
            "title": "Test Paste",
            "content": "This is a test paste.",
            "category": category.id,
            "delete_choice": "never"
        }
        form = PasteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "title": "",
            "content": "",
            "category": "",
            "delete_choice": ""
        }
        form = PasteForm(data=form_data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "content": "This is a test comment."
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "content": ""
        }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())


class CustomUserCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "password123",
            "password2": "password123"
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "password123",
            "password2": "differentpassword"
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
