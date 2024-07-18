from django.urls import reverse
from django.views.generic import CreateView, DetailView

from voidpaste.forms import PasteForm
from voidpaste.models import Paste


class PasteCreateView(CreateView):
    model = Paste
    form_class = PasteForm
    template_name = "voidpaste/index.html"

    def get_success_url(self):
        return reverse(
            "voidpaste:paste-detail",
            kwargs={"link": self.object.link}
        )


class PasteDetailView(DetailView):
    model = Paste
    template_name = "voidpaste/paste_detail.html"
    context_object_name = "paste"
    slug_field = "link"
    slug_url_kwarg = "link"
