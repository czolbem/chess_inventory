import datetime
from django.test import TestCase

from chess_utils.pgn_parser import PgnParser
from custom_exceptions.exceptions import InvalidPgnException


class PgnParserTests(TestCase):

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

    def test_pgn_parser_accepts_invalid_pgn_missing_round(self):
        # Explicitly allow invalid missing round because Lichess omits that header for some reason
        with open('resources/invalid_pgn_missing_round.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        game = PgnParser.parse(invalid_pgn_string)

        self.assertIsNotNone(game)

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

    def test_pgn_parser_rejects_invalid_pgn_missing_result(self):
        with open('resources/invalid_pgn_missing_result.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_non_numeric_date(self):
        with open('resources/invalid_pgn_non_numeric_date.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_bad_format_date(self):
        with open('resources/invalid_pgn_bad_format_date.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_bad_date(self):
        with open('resources/invalid_pgn_bad_date.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_rejects_invalid_pgn_bad_brackets(self):
        with open('resources/invalid_pgn_bad_brackets.pgn') as invalid_pgn:
            invalid_pgn_string = invalid_pgn.read()

        with self.assertRaises(InvalidPgnException):
            PgnParser.parse(invalid_pgn_string)

    def test_pgn_parser_parses_pgn_date_string_correctly(self):
        pgn_date_string = '2023.03.12'
        expected_date = datetime.date(2023, 3, 12)

        parsed_date = PgnParser.pgn_date_string_to_date(pgn_date_string)

        self.assertEqual(parsed_date, expected_date)

    def test_pgn_parser_parses_pgn_date_string_with_unknown_year_to_none(self):
        pgn_date_string = '????.03.12'
        expected_date = None

        parsed_date = PgnParser.pgn_date_string_to_date(pgn_date_string)

        self.assertEqual(parsed_date, expected_date)
