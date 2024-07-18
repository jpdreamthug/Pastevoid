from django import forms

from voidpaste.models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['title', 'content', 'category', 'delete_choice']
