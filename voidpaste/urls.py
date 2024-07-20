from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from voidpaste.views import PasteCreateView, PasteDetailView, ProfileListView, PasteUpdateView

urlpatterns = [
    path("", PasteCreateView.as_view(), name="index"),
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/$",
        PasteDetailView.as_view(),
        name="paste-detail"
    ),

    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/edit/$",
        PasteUpdateView.as_view(),
        name="paste-edit"
    ),
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

app_name = "voidpaste"
