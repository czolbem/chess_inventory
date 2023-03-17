import datetime

from django.test import TestCase

from inventory.models import Game

VALID_PGN_FILE = 'resources/valid_pgn.pgn'


class GameTests(TestCase):
    def test_saving_game_adds_data_from_pgn_to_model(self):
        with open(VALID_PGN_FILE) as pgn:
            pgn_string = pgn.read()
        description = "Test Model"
        game = Game(description=description, pgn=pgn_string)
        game.save()

        self.assertEqual(game.description, description)
        self.assertEqual(game.pgn, pgn_string)
        self.assertEqual(game.event, 'WR Chess Masters 2023')
        self.assertEqual(game.site, 'Dusseldorf GER')
        self.assertEqual(game.date, datetime.date(2023, 2, 16))
        self.assertEqual(game.round, '1')
        self.assertEqual(game.white, 'Nepomniachtchi,I')
        self.assertEqual(game.black, 'Abdusattorov,Nodirbek')
        self.assertEqual(game.result, '1/2-1/2')
        self.assertEqual(game.eco, 'A56')
        self.assertEqual(game.opening, 'Benoni')
        self.assertEqual(game.variation, None)
        self.assertEqual(game.ecot, 'A57')
        self.assertEqual(game.openingt, 'Benko gambit')
        self.assertEqual(game.variationt, 'Gambit half accepted')
