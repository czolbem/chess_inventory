from chess import COLOR_NAMES
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView

from chess_utils.chess_game import ChessGame
from chess_utils.enums import RequiredPgnHeaders, OpeningPgnHeaders
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
        date = PgnParser.pgn_date_string_to_date(date_string)

        chess_game = ChessGame(game)
        opening_information = chess_game.calculate_opening_information()

        game_model.event = game.headers.get(RequiredPgnHeaders.EVENT.value)
        game_model.site = game.headers.get(RequiredPgnHeaders.SITE.value)
        game_model.date = date
        game_model.round = game.headers.get(RequiredPgnHeaders.ROUND.value)
        game_model.white = game.headers.get(RequiredPgnHeaders.WHITE.value)
        game_model.black = game.headers.get(RequiredPgnHeaders.BLACK.value)
        game_model.result = game.headers.get(RequiredPgnHeaders.RESULT.value)
        game_model.eco = opening_information.get(OpeningPgnHeaders.ECO)
        game_model.opening = opening_information.get(OpeningPgnHeaders.OPENING)
        game_model.variation = opening_information.get(OpeningPgnHeaders.VARIATION)
        game_model.ecot = opening_information.get(OpeningPgnHeaders.ECOT)
        game_model.openingt = opening_information.get(OpeningPgnHeaders.OPENINGT)
        game_model.variationt = opening_information.get(OpeningPgnHeaders.VARIATIONT)

        game_model.save()

        return HttpResponseRedirect(reverse('game', kwargs={'pk': game_model.pk}))


class GameListView(ListView):
    model = Game
    template_name = "game_list.html"
    ordering = ['-date']


class GameDetailView(DetailView):
    model = Game
    template_name = "game_detail.html"

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        chess_game = ChessGame(PgnParser.parse(context['game'].pgn))
        context['chess_board_svg'] = chess_game.get_svg_of_last_position()
        context['turn_color'] = COLOR_NAMES[chess_game.get_last_turn_color()]
        return context
