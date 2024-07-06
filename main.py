import random

class BattleshipGame:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.player_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.player_ships = []
        self.computer_ships = []
        self.place_computer_ships()
        self.place_player_ships()

    def place_computer_ships(self):
        # Place a single ship of size 3
        self.place_ship_randomly(self.computer_board, self.computer_ships, 3)

    def place_player_ships(self):
        # Place a single ship of size 3
        print("Place your ship of size 3")
        self.print_board(self.player_board)
        self.place_ship_manually(self.player_board, self.player_ships, 3)

    def place_ship_randomly(self, board, ships_list, size):
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - size)
            else:
                row = random.randint(0, self.grid_size - size)
                col = random.randint(0, self.grid_size - 1)
            if self.can_place_ship(board, row, col, size, orientation):
                self.set_ship(board, ships_list, row, col, size, orientation)
                placed = True

    def place_ship_manually(self, board, ships_list, size):
        placed = False
        while not placed:
            orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()
            row, col = map(int, input("Enter starting position (row,col): ").split(','))
            if orientation in ['H', 'V'] and self.can_place_ship(board, row, col, size, orientation):
                self.set_ship(board, ships_list, row, col, size, orientation)
                placed = True
            else:
                print("Invalid position or orientation. Try again.")

    def can_place_ship(self, board, row, col, size, orientation):
        for i in range(size):
            if orientation == 'H':
                if col + i >= self.grid_size or board[row][col + i] != '~':
                    return False
            else:
                if row + i >= self.grid_size or board[row + i][col] != '~':
                    return False
        return True

    def set_ship(self, board, ships_list, row, col, size, orientation):
        ship_positions = []
        for i in range(size):
            if orientation == 'H':
                board[row][col + i] = 'S'
                ship_positions.append((row, col + i))
            else:
                board[row + i][col] = 'S'
                ship_positions.append((row + i, col))
        ships_list.append(ship_positions)

    def print_board(self, board, hide_ships=False):
        for row in board:
            if hide_ships:
                print(" ".join(['~' if cell == 'S' else cell for cell in row]))
            else:
                print(" ".join(row))

    def get_guess(self):
        while True:
            guess = input("Enter your guess (row,col): ")
            row, col = map(int, guess.split(','))
            if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                return row, col
            else:
                print("Guess is off-grid. Try again.")

    def computer_guess(self):
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if self.player_board[row][col] == '~' or self.player_board[row][col] == 'S':
                return row, col

    def check_guess(self, board, ships_list, row, col):
        if board[row][col] == 'S':
            board[row][col] = 'X'
            print("Hit!")
            for ship in ships_list:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        ships_list.remove(ship)
                        print("Ship sunk!")
                    break
        elif board[row][col] == '~':
            board[row][col] = 'O'
            print("Miss!")
        else:
            print("Already guessed that. Try again.")

    def is_game_over(self, ships_list):
        return len(ships_list) == 0

    def play(self):
        print("Welcome to Battleship!")
        while True:
            print("\nYour board:")
            self.print_board(self.player_board)
            print("\nComputer's board:")
            self.print_board(self.computer_board, hide_ships=True)

            # Player's turn
            print("\nPlayer's turn:")
            row, col = self.get_guess()
            self.check_guess(self.computer_board, self.computer_ships, row, col)
            if self.is_game_over(self.computer_ships):
                print("Congratulations! You sunk all the computer's battleships!")
                break

            # Computer's turn
            print("\nComputer's turn:")
            row, col = self.computer_guess()
            print(f"Computer guessed: {row},{col}")
            self.check_guess(self.player_board, self.player_ships, row, col)
            if self.is_game_over(self.player_ships):
                print("Game over! The computer sunk all your battleships!")
                break

def main():
    print("Welcome to the Battleship game!")
    while True:
        start_game = input("Would you like to start the game? (y/n): ").lower()
        if start_game == 'y':
            game = BattleshipGame()
            game.play()
        elif start_game == 'n':
            print("Maybe next time!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'n':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
