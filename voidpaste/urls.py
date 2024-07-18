from django.urls import path

from voidpaste.views import PasteCreateView

urlpatterns = [
    path("", PasteCreateView.as_view(), name="index"),
]

app_name = "voidpaste"
