from django import forms
from django.contrib.auth.forms import UserCreationForm

from voidpaste.models import Paste, User, Comment


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ["content", "title", "category", "delete_choice"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Enter your Paste, probably Void",
                    "rows": 20,
                    "cols": 50,
                }
            ),
            "title": forms.TextInput(
                attrs={"placeholder": "Enter title here"}
            ),
            "category": forms.Select(
                attrs={"placeholder": "Select a category"}
            ),
        }
        labels = {
            "content": "",
            "title": "Paste name/Title",
            "delete_choice": "Expires at",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Type your comment here...",
                    "class": "form-control",
                }
            ),
        }
        labels = {
            "content": "",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({"autofocus": "autofocus"})


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
