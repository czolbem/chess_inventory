from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView

from inventory.forms import GameForm
from inventory.models import Game


class HomeView(TemplateView):
    template_name = "home.html"


class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm
    # TODO change this to something better
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super(GameFormView, self).form_valid(form)


class GameListView(ListView):
    model = Game
    template_name = "game_list.html"
