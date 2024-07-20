from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from voidpaste.forms import PasteForm
from voidpaste.models import Paste, Comment


class PasteCreateView(CreateView):
    model = Paste
    form_class = PasteForm
    template_name = "voidpaste/index.html"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "voidpaste:paste-detail",
            kwargs={"link": self.object.link}
        )


class PasteDetailView(DetailView):
    model = Paste
    slug_field = "link"
    slug_url_kwarg = "link"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["comments"] = Comment.objects.select_related("user").select_related("paste")
        return context


class ProfileListView(LoginRequiredMixin, ListView):
    model = Paste
    template_name = "voidpaste/profile.html"
    context_object_name = "pastes"

    def get_queryset(self):
        return Paste.objects.filter(user=self.request.user)


class PasteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paste
    form_class = PasteForm
    template_name = "voidpaste/index.html"
    success_url = reverse_lazy("voidpaste:profile")

    def get_object(self, queryset=None):
        queryset = Paste.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        link = self.kwargs.get("link")
        return get_object_or_404(queryset, link=link)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields.pop('category', None)
        form.fields.pop('delete_choice', None)
        return form


class PasteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paste

    def get_success_url(self):
        return reverse_lazy('voidpaste:profile')

    def get_object(self, queryset=None):
        queryset = Paste.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        link = self.kwargs.get("link")
        return get_object_or_404(queryset, link=link)


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("voidpaste:index")

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)
        return super().form_valid(form)
