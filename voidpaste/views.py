from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from voidpaste.forms import (
    PasteForm,
    CustomUserCreationForm,
    CommentForm
)
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
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.all().order_by("-created_at")
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["comments"] = page_obj
        context["comment_form"] = CommentForm()
        context["page_obj"] = page_obj
        return context


class ProfileListView(LoginRequiredMixin, ListView):
    model = Paste
    template_name = "voidpaste/profile.html"
    context_object_name = "pastes"
    paginate_by = 5

    def get_queryset(self):
        return Paste.objects.filter(
            user=self.request.user
        ).order_by("-created_at")


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
        form.fields.pop("category", None)
        form.fields.pop("delete_choice", None)
        return form


class PasteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paste

    def get_success_url(self):
        return reverse_lazy("voidpaste:profile")

    def get_object(self, queryset=None):
        queryset = Paste.objects.all()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)
        link = self.kwargs.get("link")
        return get_object_or_404(queryset, link=link)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "voidpaste/paste_detail.html"

    def form_valid(self, form):
        paste = get_object_or_404(Paste, link=self.kwargs["link"])
        form.instance.paste = paste
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "voidpaste:paste-detail",
            kwargs={"link": self.kwargs["link"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paste = get_object_or_404(Paste, link=self.kwargs["link"])
        context["paste"] = paste
        context["comments"] = paste.comments.all().order_by("-created_at")
        return context


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("voidpaste:index")

    def form_valid(self, form):
        remember_me = self.request.POST.get("remember_me")
        if not remember_me:
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(1209600)
        return super().form_valid(form)


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("voidpaste:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
