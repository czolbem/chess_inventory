import chess.pgn
import chess.svg


class ChessGame:
    game: chess.pgn.Game = None

    def __init__(self, game: chess.pgn.Game) -> None:
        self.game = game

    def get_svg_of_last_position(self) -> str:
        board_at_end_position = self.game.end().board()
        return chess.svg.board(board_at_end_position)

    def get_last_turn_color(self) -> chess.pgn.Color:
        return self.game.end().board().turn
