import datetime
import io
import logging
import chess.pgn

from chess_utils.enums import RequiredPgnHeaders
from custom_exceptions.exceptions import InvalidPgnException


class PgnParser:
    @staticmethod
    def parse(pgn: str) -> chess.pgn.Game:
        if not PgnParser.is_pgn_valid(pgn):
            raise InvalidPgnException('PGN is not valid')
        game = chess.pgn.read_game(io.StringIO(pgn))
        if not PgnParser.is_game_valid(game):
            raise InvalidPgnException('PGN contains a game that is not valid')
        if not PgnParser.is_date_valid(game, RequiredPgnHeaders.DATE.value):
            raise InvalidPgnException('PGN contains invalid date')
        return game

    @staticmethod
    def is_game_valid(game: chess.pgn.Game) -> bool:
        if game.errors:
            return False
        return True

    @staticmethod
    def is_pgn_valid(pgn: str) -> bool:
        """
        The library used to parse PGN is very forgiving with malformed and invalid PGN.
        This function adds some custom validation to make sure basic constraints are followed.
        This follows the stricter export format, instead of the less restrictive import format, see:
        http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm#c8.1.1
        :param pgn: The PGN string
        :return: If the PGN is valid or not
        """
        tag_names = []
        pgn_io = io.StringIO(pgn)
        try:
            for line in pgn_io:
                line = line.strip()
                if line == '':
                    break
                if line[0] != '[' or line[-1] != ']':
                    return False
                tag_names.append(line.split(' ')[0][1:])
        except IndexError:
            return False

        for header in RequiredPgnHeaders:
            # Explicitly allow missing round because Lichess omits it for some reason
            if header is not RequiredPgnHeaders.ROUND and header.value not in tag_names:
                logging.debug(f'Required header {header.value} not found in PGN')
                return False

        return True

    @staticmethod
    def is_date_valid(game: chess.pgn.Game, date_tag_name: str) -> bool:
        """
        Checking a date for compliance with the insane pgn standard date format:
        '2023.03.12' where any unknown value can be replaced by question marks
        """
        try:
            date_string = game.headers.get(date_tag_name)
        except KeyError:
            return False
        date_split = date_string.split('.')
        if len(date_split) != 3:
            return False
        year = 2023
        month = 1
        day = 1
        game_year = date_split[0]
        game_month = date_split[1]
        game_day = date_split[2]
        try:
            if '?' not in game_year:
                year = int(game_year)
            if '?' not in game_month:
                month = int(game_month)
            if '?' not in game_day:
                day = int(game_day)
        except ValueError:
            return False

        try:
            datetime.date(year, month, day)
        except ValueError:
            return False

        return True

    @staticmethod
    def pgn_date_string_to_date(date_string: str) -> datetime.date:
        date_split = date_string.split('.')
        year = None
        month = 1
        day = 1
        if '?' not in date_split[0]:
            year = int(date_split[0])
        if '?' not in date_split[1]:
            month = int(date_split[1])
        if '?' not in date_split[2]:
            day = int(date_split[2])
        if year is None:
            date = None
        else:
            date = datetime.date(year, month, day)
        return date
