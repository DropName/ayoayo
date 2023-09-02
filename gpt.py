class AyoayoGame:
    def __init__(self):
        self.board = [4] * 12  # Initialize the board with 4 seeds in each hole
        self.current_player = 0  # Player 1 starts (0-based index)

    def display_board(self):
        print(f"Player 1: {self.board[:6]}")
        print(f"Player 2: {self.board[6:]}")

    def make_move(self, hole):
        if hole < 0 or hole >= 12 or self.board[hole] == 0:
            print("Invalid move. Try again.")
            return False

        seeds_to_sow = self.board[hole]
        self.board[hole] = 0

        while seeds_to_sow > 0:
            if hole != 6:  # Skip the opponent's store
                self.board[hole] += 1
                seeds_to_sow -= 1

        self.capture_seeds(hole)
        self.check_for_winner()
        self.switch_player()
        return True

    def capture_seeds(self, last_hole):
        if self.board[last_hole] == 1 and self.board[(11 - last_hole)] > 0:
            self.board[6] += self.board[last_hole] + self.board[(11 - last_hole)]
            self.board[last_hole] = 0
            self.board[(11 - last_hole)] = 0

    def check_for_winner(self):
        if all(seeds == 0 for seeds in self.board[:6]):
            self.board[6] += sum(self.board[7:])
            self.display_board()
            print("Player 2 wins!")
            exit()
        elif all(seeds == 0 for seeds in self.board[7:]):
            self.board[13] += sum(self.board[:6])
            self.display_board()
            print("Player 1 wins!")
            exit()

    def switch_player(self):
        self.current_player = 1 - self.current_player

def main():
    game = AyoayoGame()
    while True:
        game.display_board()
        player_input = input(f"Player {game.current_player + 1}, choose a hole to move (0-11): ")
        try:
            hole = int(player_input)
            if game.make_move(hole):
                continue
        except ValueError:
            pass
        print("Invalid input. Please enter a valid hole number (0-11).")

if __name__ == "main":
    main()
