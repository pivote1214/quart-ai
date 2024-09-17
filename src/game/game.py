import random
from itertools import product

from src.game.board import Board
from src.game.piece import COLORS, HEIGHTS, HOLES, SHAPES, Piece
from src.player.baseline import Baseline
from src.player.player import Player


class Game:
    """
    QUARTのゲームを表すクラス
    """
    def __init__(self, player1: Player, player2: Player) -> None:
        self.board = Board()
        self.players = [player1, player2]
        self.available_pieces: list[Piece] = [Piece(color, height, shape, hole) 
                                              for color, height, shape, hole in product(COLORS, HEIGHTS, SHAPES, HOLES)]
        random.shuffle(self.available_pieces)

    def play(self) -> None:
        """
        ゲームを実行します。
        """
        current_player_idx = 0
        selected_piece = None

        while True:
            current_player = self.players[current_player_idx]
            # other_player = self.players[1 - current_player_idx]

            if selected_piece is None:
                # ゲーム開始時に最初のプレイヤーがコマを選ぶ
                selected_piece = current_player.select_piece(self.available_pieces)
                self.available_pieces.remove(selected_piece)
                print(f"{current_player.name} がコマを選択: {selected_piece}")
                current_player_idx = 1 - current_player_idx
                continue

            # コマを配置
            position = current_player.place_piece(self.board, selected_piece)
            print(f"{current_player.name} がコマ {selected_piece} を位置 {position} に配置")
            print(self.board)

            # 勝利チェック
            if self.board.check_victory():
                print(f"{current_player.name} が『クアルト』を宣言して勝利！")
                break

            if self.board.is_full():
                print("盤面が埋まりました。引き分けです。")
                break

            # 次のプレイヤーがコマを選ぶ
            selected_piece = current_player.select_piece(self.available_pieces)
            self.available_pieces.remove(selected_piece)
            print(f"{current_player.name} が次のコマを選択: {selected_piece}")

            current_player_idx = 1 - current_player_idx

# ゲームの実行例
if __name__ == "__main__":
    player1 = Baseline(name="Baseline 1")
    player2 = Baseline(name="Baseline 2")  # もう一人のAIを追加
    game = Game(player1, player2)
    game.play()
