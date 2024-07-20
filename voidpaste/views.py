from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from voidpaste.forms import PasteForm
from voidpaste.models import Paste


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


class ProfileListView(LoginRequiredMixin, ListView):
    model = Paste
    template_name = "voidpaste/profile.html"
    context_object_name = "pastes"

    def get_queryset(self):
        return Paste.objects.filter(user=self.request.user)


class PasteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paste
    fields = ("content",)


class PasteDeleteView(LoginRequiredMixin, DeleteView):
    ...
