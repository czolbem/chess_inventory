import io

import chess.pgn

from chess_utils.enums import RequiredPgnHeaders
from custom_exceptions.exceptions import InvalidPgnException


class PgnParser:
    @staticmethod
    def parse(pgn: str) -> chess.pgn.Game:
        game = chess.pgn.read_game(io.StringIO(pgn))
        if not PgnParser.is_valid(game):
            raise InvalidPgnException()
        return game

    @staticmethod
    def is_valid(game: chess.pgn.Game) -> bool:
        if game.errors:
            return False

        for header in RequiredPgnHeaders:
            if game.headers.get(header.value) in ('?', '????.??.??', '?-?'):
                return False

        return True
