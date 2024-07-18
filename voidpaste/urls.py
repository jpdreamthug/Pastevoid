from django.urls import path

from voidpaste.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "voidpaste"