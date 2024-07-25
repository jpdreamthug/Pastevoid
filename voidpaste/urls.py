from django.contrib.auth.views import LogoutView
from django.urls import path, re_path

from voidpaste.views import (
    PasteCreateView,
    PasteDetailView,
    ProfileListView,
    PasteUpdateView,
    PasteDeleteView,
    CustomLoginView,
    RegisterView,
    CommentCreateView,
)

urlpatterns = [
    path(
        "",
        PasteCreateView.as_view(),
        name="index"
    ),
    path(
        "profile/",
        ProfileListView.as_view(),
        name="profile"),
    path(
        "logout/",
        LogoutView.as_view(next_page="/"),
        name="logout"
    ),
    path(
        "login/",
        CustomLoginView.as_view(),
        name="login"
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/$",
        PasteDetailView.as_view(),
        name="paste-detail"
    ),
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/edit/$",
        PasteUpdateView.as_view(),
        name="paste-edit",
    ),
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/delete/$",
        PasteDeleteView.as_view(),
        name="paste-delete",
    ),
    re_path(
        r"^(?P<link>[a-zA-Z0-9]{8})/comment/$",
        CommentCreateView.as_view(),
        name="add-comment",
    ),
]

app_name = "voidpaste"
