import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView

from chess_utils.enums import RequiredPgnHeaders
from chess_utils.pgn_parser import PgnParser
from inventory.forms import GameForm
from inventory.models import Game


class HomeView(TemplateView):
    template_name = "home.html"


class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm

    def form_valid(self, form) -> HttpResponseRedirect:
        game_model = form.save(commit=False)
        game = PgnParser.parse(game_model.pgn)

        date_string = game.headers.get(RequiredPgnHeaders.DATE.value)
        date_split = date_string.split('.')
        year = None
        month = 1
        day = 1
        if '?' not in date_split[0]:
            year = int(date_split[0])
        if '?' not in date_split[1]:
            month = int(date_split[1])
        if '?' not in date_split[2]:
            day = int(date_split[2])

        if year is None:
            date = None
        else:
            date = datetime.date(year, month, day)

        game_model.event = game.headers.get(RequiredPgnHeaders.EVENT.value)
        game_model.site = game.headers.get(RequiredPgnHeaders.SITE.value)
        game_model.date = date
        game_model.round = game.headers.get(RequiredPgnHeaders.ROUND.value)
        game_model.white = game.headers.get(RequiredPgnHeaders.WHITE.value)
        game_model.black = game.headers.get(RequiredPgnHeaders.BLACK.value)
        game_model.result = game.headers.get(RequiredPgnHeaders.RESULT.value)

        game_model.save()

        return HttpResponseRedirect(reverse('game', kwargs={'pk': game_model.pk}))


class GameListView(ListView):
    model = Game
    template_name = "game_list.html"


class GameDetailView(DetailView):
    model = Game
    template_name = "game_detail.html"
