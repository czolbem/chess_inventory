from django.test import TestCase

import chess.pgn

from chess_utils.chess_game import ChessGame
from chess_utils.enums import OpeningPgnHeaders
from chess_utils.pgn_parser import PgnParser

VALID_PGN_FILE = 'resources/valid_pgn.pgn'


class ChessGameTests(TestCase):
    def test_chess_game_initialises_game(self):
        game = chess.pgn.Game()
        chess_game = ChessGame(game)

        self.assertEqual(chess_game.game, game)

    def test_get_svg_of_last_position_returns_correct_svg(self):
        with open(VALID_PGN_FILE) as pgn:
            game = PgnParser.parse(pgn.read())
        with open('resources/svg_of_last_posititon.txt') as svg:
            svg_actual = svg.read()
        chess_game = ChessGame(game)

        svg_of_last_position = chess_game.get_svg_of_last_position()

        self.assertEqual(svg_of_last_position, svg_actual)

    def test_get_last_turn_colour_returns_correct_colour(self):
        with open(VALID_PGN_FILE) as pgn:
            game = PgnParser.parse(pgn.read())
        chess_game = ChessGame(game)

        last_turn_colour = chess_game.get_last_turn_color()

        self.assertEqual(last_turn_colour, chess.BLACK)

    def test_calculate_opening_returns_correct_opening(self):
        with open(VALID_PGN_FILE) as pgn:
            game = PgnParser.parse(pgn.read())
        chess_game = ChessGame(game)
        expected_opening_information = {
            OpeningPgnHeaders.ECO: 'A56',
            OpeningPgnHeaders.OPENING: 'Benoni',
            OpeningPgnHeaders.VARIATION: None,
            OpeningPgnHeaders.ECOT: 'A57',
            OpeningPgnHeaders.OPENINGT: 'Benko gambit',
            OpeningPgnHeaders.VARIATIONT: 'Gambit half accepted'
        }

        opening_information = chess_game.calculate_opening_information()

        self.assertEqual(opening_information, expected_opening_information)
