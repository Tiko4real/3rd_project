import random

class BattleshipGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_board = [['~' for _ in range(grid_size)] for _ in range(grid_size)]
        self.ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        self.place_ships()

    def place_ships(self):
        for size in self.ships.values():
            self.place_ship_randomly(size)
 