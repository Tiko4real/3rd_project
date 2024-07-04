import random

class BattleshipGame:
    #This function  create the grind net for the game and placement logics"
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        self.place_ships()

    def place_ships(self):
        for size in self.ships.values():
            self.place_ship_randomly(size)
    def place_ship_randomly(self, size):
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - size)
            else:
                row = random.randint(0, self.grid_size - size)
                col = random.randint(0, self.grid_size - 1)
            if self.can_place_ship(row, col, size, orientation):
                self.set_ship(row, col, size, orientation)
                placed = True

    def can_place_ship(self, row, col, size, orientation):
        for i in range(size):
            if orientation == 'H':
                if self.computer_board[row][col + i] != '~':
                    return False
            else:
                if self.computer_board[row + i][col] != '~':
                    return False
        return True

    def set_ship(self, row, col, size, orientation):
        for i in range(size):
            if orientation == 'H':
                self.computer_board[row][col + i] = 'S'
            else:
                self.computer_board[row + i][col] = 'S',
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

    def check_gues(self, row, col):
        if self.computer_board[row][col] == 'S':
            self.player_board[row][col] = 'X'
            self.computer_board[row][col] = 'X'
            print("Hit!")
        elif self.computer_board[row][col] == '~':
            self.player_board[row][col] = 'O'
            self.computer_board[row][col] = 'O'
            print("Miss!")
        else:
            print("Already guessed that. Try again.")

    def is_game_over(self):
        for row in self.computer_board:
            if 'S' in row:
                return False
        return True

