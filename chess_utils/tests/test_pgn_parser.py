from unittest import TestCase

from chess_utils.pgn_parser import PgnParser
from custom_exceptions.exceptions import InvalidPgnException


class MyTestCase(TestCase):

    def test_pgn_parser_can_parse_valid_pgn(self):
        with open('resources/valid_pgn.pgn') as valid_pgn:
            valid_pgn_string = valid_pgn.read()

        game = PgnParser.parse(valid_pgn_string)

        self.assertIsNotNone(game)

    def test_pgn_parser_rejects_invalid_pgn_with_errors(self):
        with open('resources/invalid_pgn_illegal_move.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_event(self):
        with open('resources/invalid_pgn_missing_event.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_site(self):
        with open('resources/invalid_pgn_missing_site.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_date(self):
        with open('resources/invalid_pgn_missing_date.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_round(self):
        with open('resources/invalid_pgn_missing_round.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_white(self):
        with open('resources/invalid_pgn_missing_white.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_missing_black(self):
        with open('resources/invalid_pgn_missing_black.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_infers_missing_result_header_from_moves(self):
        with open('resources/pgn_missing_result.pgn') as pgn:
            pgn_string = pgn.read()

        game = PgnParser.parse(pgn_string)

        self.assertEqual('1/2-1/2', game.headers.get('Result'))
