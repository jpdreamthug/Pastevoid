from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, re_path

from voidpaste.views import (
    PasteCreateView,
    PasteDetailView,
    ProfileListView,
    PasteUpdateView,
    PasteDeleteView, CustomLoginView,
)

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
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/delete/$",
        PasteDeleteView.as_view(),
        name="paste-delete"
    ),
    path('profile/', ProfileListView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login')
]

app_name = "voidpaste"
