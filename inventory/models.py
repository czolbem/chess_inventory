from django.db import models

from chess_inventory.validators import validate_pgn
from chess_utils.chess_game import ChessGame
from chess_utils.enums import RequiredPgnHeaders, OpeningPgnHeaders
from chess_utils.pgn_parser import PgnParser


class Game(models.Model):
    pgn = models.TextField(validators=[validate_pgn])
    description = models.CharField(max_length=100, default='', blank=True)
    event = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    date = models.DateField(null=True)
    round = models.CharField(max_length=20)
    white = models.CharField(max_length=100)
    black = models.CharField(max_length=100)
    result = models.CharField(max_length=10)
    eco = models.CharField(max_length=10, null=True)
    opening = models.CharField(max_length=100, null=True)
    variation = models.CharField(max_length=100, null=True)
    ecot = models.CharField(max_length=10, null=True)
    openingt = models.CharField(max_length=100, null=True)
    variationt = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        game = PgnParser.parse(self.pgn)
        date_string = game.headers.get(RequiredPgnHeaders.DATE.value)
        date = PgnParser.pgn_date_string_to_date(date_string)
        chess_game = ChessGame(game)
        opening_information = chess_game.calculate_opening_information()
        self.event = game.headers.get(RequiredPgnHeaders.EVENT.value)
        self.site = game.headers.get(RequiredPgnHeaders.SITE.value)
        self.date = date
        self.round = game.headers.get(RequiredPgnHeaders.ROUND.value)
        self.white = game.headers.get(RequiredPgnHeaders.WHITE.value)
        self.black = game.headers.get(RequiredPgnHeaders.BLACK.value)
        self.result = game.headers.get(RequiredPgnHeaders.RESULT.value)
        self.eco = opening_information.get(OpeningPgnHeaders.ECO)
        self.opening = opening_information.get(OpeningPgnHeaders.OPENING)
        self.variation = opening_information.get(OpeningPgnHeaders.VARIATION)
        self.ecot = opening_information.get(OpeningPgnHeaders.ECOT)
        self.openingt = opening_information.get(OpeningPgnHeaders.OPENINGT)
        self.variationt = opening_information.get(OpeningPgnHeaders.VARIATIONT)
        super(Game, self).save(*args, **kwargs)
