from django import forms
from voidpaste.models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ["content", "title", "category", "delete_choice"]
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter your Paste, probably Void',
                'rows': 20,
                'cols': 50
            }),
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'category': forms.Select(attrs={'placeholder': 'Select a category'}),
        }
        labels = {
            'content': '',
            'title': "Paste name/Title",
            "delete_choice": "Expires at"
        }
