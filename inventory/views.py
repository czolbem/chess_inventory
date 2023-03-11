from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from inventory.forms import GameForm


class HomeView(TemplateView):
    template_name = "home.html"


class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm
    # TODO change this to something better
    success_url = reverse_lazy('home')
