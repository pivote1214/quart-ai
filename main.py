# main.py

from game.game_state import GameState
from agent.baseline import BaselineAgent


def display_available_pieces(pieces):
    print("Available pieces:")
    for idx, piece in enumerate(pieces):
        print(f"{idx}: {piece}")

def get_piece_choice(pieces):
    while True:
        try:
            idx = int(input("Select a piece: "))
            if 0 <= idx < len(pieces):
                return pieces[idx]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def get_position_choice(empty_positions):
    while True:
        try:
            x = int(input("x-coordinate to place the piece (0-3): "))
            y = int(input("y-coordinate to place the piece (0-3): "))
            if (x, y) in empty_positions:
                return x, y
            else:
                print("Cannot place a piece in that position. Please try again.")
        except ValueError:
            print("Please enter a number.")

def main():
    game_state = GameState()

    # Select game mode
    print("Select a game mode:")
    print("1: Human vs Baseline Agent")
    print("2: Human vs Human")
    mode = input("Enter the mode number: ")

    if mode == '1':
        agent = BaselineAgent(player_number=1)  # Agent plays as Player 2
        human_player_number = 0
    elif mode == '2':
        agent = None
        human_player_number = None
    else:
        print("Invalid mode. Defaulting to Human vs Baseline Agent mode.")
        agent = BaselineAgent(player_number=1)
        human_player_number = 0

    while not game_state.is_game_over():
        print(game_state)
        current_player = game_state.turn

        if current_player == human_player_number:
            # Human player's turn
            if game_state.next_piece is None:
                # Choose a piece to give to the opponent
                display_available_pieces(game_state.available_pieces)
                selected_piece = get_piece_choice(game_state.available_pieces)
                game_state.set_next_piece(selected_piece)
            else:
                # Place the piece on the board
                print(f"Your turn. Piece passed from the opponent: {game_state.next_piece}")
                empty_positions = game_state.board.get_empty_positions()
                x, y = get_position_choice(empty_positions)
                game_state.place_next_piece(x, y)

                if game_state.board.check_victory():
                    print(game_state.board)
                    print(f"Player {current_player + 1} wins!")
                    return
        else:
            # Agent's or second human player's turn
            if agent is not None:
                # Agent's turn
                if game_state.next_piece is None:
                    # Choose a piece to give to the opponent
                    selected_piece = agent.select_piece(game_state)
                    print(f"The agent passes you the piece: {selected_piece}")
                    game_state.set_next_piece(selected_piece)
                else:
                    # Place the piece on the board
                    print(f"Agent's turn. Piece you passed: {game_state.next_piece}")
                    x, y = agent.select_placement(game_state)
                    game_state.place_next_piece(x, y)
                    print(f"Agent placed a piece at position: ({x}, {y})")

                    if game_state.board.check_victory():
                        print(game_state.board)
                        print("The agent wins!")
                        return
            else:
                # Second human player's turn
                print(f"Player {current_player + 1}'s turn.")
                if game_state.next_piece is None:
                    # Choose a piece to give to the opponent
                    display_available_pieces(game_state.available_pieces)
                    selected_piece = get_piece_choice(game_state.available_pieces)
                    game_state.set_next_piece(selected_piece)
                else:
                    # Place the piece on the board
                    print(f"Player {current_player + 1}'s turn. Piece passed from the opponent: {game_state.next_piece}")
                    empty_positions = game_state.board.get_empty_positions()
                    x, y = get_position_choice(empty_positions)
                    game_state.place_next_piece(x, y)

                    if game_state.board.check_victory():
                        print(game_state.board)
                        print(f"Player {current_player + 1} wins!")
                        return

    print("Game over. It's a draw.")


if __name__ == "__main__":
    main()
