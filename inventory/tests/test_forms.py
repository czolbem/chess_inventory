from django.test import TestCase

from inventory.forms import GameForm


class FormTests(TestCase):
    def test_game_form_accepts_valid_pgn(self):
        with open('resources/valid_pgn.pgn') as valid_pgn:
            game_form = GameForm(data={'description': "Test Form", 'pgn': valid_pgn.read()})
            self.assertTrue(game_form.is_valid())

    def test_game_form_rejects_invalid_pgn(self):
        with open('resources/invalid_pgn_illegal_move.pgn') as invalid_pgn:
            game_form = GameForm(data={'description': "Test Form", 'pgn': invalid_pgn.read()})

        self.assertFalse(game_form.is_valid())
