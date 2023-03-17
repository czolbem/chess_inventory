from django.test import TestCase

from inventory.serializers import GameSerializer


class SerializerTests(TestCase):
    def test_game_serializer_accepts_valid_pgn(self):
        with open('resources/valid_pgn.pgn') as valid_pgn:
            game_serializer = GameSerializer(data={'description': "Test Form", 'pgn': valid_pgn.read()})

        self.assertTrue(game_serializer.is_valid())

    def test_game_serializer_rejects_invalid_pgn(self):
        with open('resources/invalid_pgn_illegal_move.pgn') as invalid_pgn:
            game_serializer = GameSerializer(data={'description': "Test Form", 'pgn': invalid_pgn.read()})

        self.assertFalse(game_serializer.is_valid())
