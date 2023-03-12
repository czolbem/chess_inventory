from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView

from inventory.forms import GameForm
from inventory.models import Game


class HomeView(TemplateView):
    template_name = "home.html"


class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm

    def form_valid(self, form) -> HttpResponseRedirect:
        # todo validation and enrichment of model here
        game = form.save()
        return HttpResponseRedirect(reverse('game', kwargs={'pk': game.pk}))


class GameListView(ListView):
    model = Game
    template_name = "game_list.html"


class GameDetailView(DetailView):
    model = Game
    template_name = "game_detail.html"
