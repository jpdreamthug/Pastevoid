from django.shortcuts import render
from django.views.generic import CreateView

from voidpaste.models import Paste


class PasteCreateView(CreateView):
    model = Paste
