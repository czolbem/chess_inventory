import logging
from typing import Any

import chess.pgn
import chess.svg
import chess.polyglot

from chess_utils.enums import OpeningPgnHeaders


class ChessGame:
    game: chess.pgn.Game = None

    def __init__(self, game: chess.pgn.Game) -> None:
        self.game = game

    def get_svg_of_last_position(self) -> str:
        board_at_end_position = self.game.end().board()
        return chess.svg.board(board_at_end_position)

    def get_last_turn_color(self) -> chess.pgn.Color:
        return self.game.end().board().turn

    def calculate_opening_information(self) -> dict[OpeningPgnHeaders, Any | None]:
        # This is based on code from https://github.com/fsmosca/pgnhelper
        # Maybe cache this somehow?
        logging.debug('Calculating opening information')
        eco_db = self.__create_eco_db()
        ply = 4
        maxply = 24

        first_eco, eco_t = None, None
        first_opening, opening_t = None, None
        first_variation, variation_t = None, None
        for node in self.game.mainline():
            board = node.board()
            gply = board.ply()
            epd = board.epd()

            # After the first move check the position if it is in eco db.
            if gply >= 1:
                if epd in eco_db:

                    # Update first eco up to a given ply only.
                    if gply <= ply:
                        first_eco = eco_db[epd]['eco']
                        first_opening = eco_db[epd]['opening']
                        first_variation = eco_db[epd]['variation']

                    # Else update eco by transposition.
                    else:
                        eco_t = eco_db[epd]['eco']
                        opening_t = eco_db[epd]['opening']
                        variation_t = eco_db[epd]['variation']

                if gply >= maxply:
                    break

        opening_information = {
            OpeningPgnHeaders.ECO: first_eco,
            OpeningPgnHeaders.OPENING: first_opening,
            OpeningPgnHeaders.VARIATION: first_variation,
            OpeningPgnHeaders.ECOT: eco_t,
            OpeningPgnHeaders.OPENINGT: opening_t,
            OpeningPgnHeaders.VARIATIONT: variation_t
        }

        return opening_information

    @staticmethod
    def __create_eco_db() -> dict[str, dict[str, str | None]]:
        logging.debug('Creating opening database from scratch')
        eco_db = {}
        with open('resources/eco.pgn', 'r') as eco_pgn:
            while True:
                game = chess.pgn.read_game(eco_pgn)
                if game is None:
                    break
                try:
                    eco = game.headers['ECO']
                except KeyError:
                    continue
                try:
                    opening = game.headers['Opening']
                except KeyError:
                    continue
                try:
                    variation = game.headers['Variation']
                except KeyError:
                    variation = None
                node = game
                node_end = node.end()
                end_board = node_end.board()
                epd = end_board.epd()
                eco_db.update({epd: {'eco': eco, 'opening': opening, 'variation': variation}})
        return eco_db
