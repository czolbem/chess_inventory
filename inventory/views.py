from chess import COLOR_NAMES
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, DetailView

from chess_utils.chess_game import ChessGame
from chess_utils.pgn_parser import PgnParser
from inventory.forms import GameForm
from inventory.models import Game
from rest_framework import viewsets

from inventory.serializers import GameSerializer


class HomeView(TemplateView):
    template_name = "home.html"


class GameFormView(FormView):
    template_name = "game_form.html"
    form_class = GameForm

    def form_valid(self, form) -> HttpResponseRedirect:
        game_model = form.save()

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


class GameViewSet(viewsets.ModelViewSet):
    model = Game
    queryset = Game.objects.all().order_by('-date')
    serializer_class = GameSerializer
