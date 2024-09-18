# ai/baseline_agent.py

import random

from game.game_state import GameState


class BaselineAgent:
    def __init__(self, player_number):
        self.player_number = player_number  # 0: プレイヤー1, 1: プレイヤー2

    def select_placement(self, game_state: GameState):
        """
        select placement for the next piece
        - if there is a winning move, select that move
        - otherwise, select a random move
        """
        board = game_state.board
        piece = game_state.next_piece
        empty_positions = board.get_empty_positions()

        # 勝てる位置を探す
        for position in empty_positions:
            x, y = position
            # 仮にコマを置いて勝利判定を行う
            board.grid[x][y] = piece
            if board.check_victory():
                board.grid[x][y] = None  # 盤面を元に戻す
                return x, y  # 勝てる位置を返す
            board.grid[x][y] = None  # 盤面を元に戻す

        # 勝てない場合はランダムに配置
        return random.choice(empty_positions)

    def select_piece(self, game_state: GameState):
        """
        select a piece to pass to the opponent
        """
        available_pieces = game_state.available_pieces
        return random.choice(available_pieces)
