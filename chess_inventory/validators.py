from django.core.exceptions import ValidationError

from chess_utils.pgn_parser import PgnParser
from custom_exceptions.exceptions import InvalidPgnException


def validate_pgn(pgn: str) -> None:
    try:
        PgnParser.parse(pgn)
    except InvalidPgnException:
        raise ValidationError("PGN is not valid")
