from django.urls import path, re_path

from voidpaste.views import PasteCreateView, PasteDetailView

urlpatterns = [
    path("", PasteCreateView.as_view(), name="index"),
    re_path(r'^(?P<link>[a-zA-Z0-9]{8})/$', PasteDetailView.as_view(), name='paste-detail'),

]

app_name = "voidpaste"
