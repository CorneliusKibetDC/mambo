
import random

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [["~"] * size for _ in range(size)]  # "~" represents water
        self.ship_sizes = [5, 4, 3, 3, 2]  # Sizes of ships
        self.ships = []  # To store ship coordinates

    def place_ship(self, size):
        """Attempts to place a ship of a given size on the board randomly."""
        for _ in range(100):  # Try 100 times to place the ship
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - size)
                coordinates = [(x, y + i) for i in range(size)]
            else:  # vertical
                x = random.randint(0, self.size - size)
                y = random.randint(0, self.size - 1)
                coordinates = [(x + i, y) for i in range(size)]

            # Check if the ship overlaps with existing ships
            if all(self.grid[x][y] == "~" for x, y in coordinates):
                for x, y in coordinates:
                    self.grid[x][y] = "S"
                self.ships.append(coordinates)
                return True
        return False

    def place_all_ships(self):
        """Places all ships on the board randomly based on the defined sizes."""
        for size in self.ship_sizes:
            if not self.place_ship(size):
                raise RuntimeError("Unable to place all ships on the board.")

    def manual_place_ship(self, size):
        """Allows the player to manually place a ship of a given size."""
        while True:
            try:
                print(f"Placing ship of size {size}.")
                coordinates = input("Enter starting coordinates (row col): ").split()
                x, y = int(coordinates[0]), int(coordinates[1])
                direction = input("Enter direction (horizontal/vertical): ").lower()

                # Validate input
                if direction not in ["horizontal", "vertical"]:
                    print("Invalid direction. Please enter 'horizontal' or 'vertical'.")
                    continue

                if direction == "horizontal":
                    if y + size > self.size:
                        print("Ship goes out of bounds horizontally. Try again.")
                        continue
                    ship_coords = [(x, y + i) for i in range(size)]
                else:  # vertical
                    if x + size > self.size:
                        print("Ship goes out of bounds vertically. Try again.")
                        continue
                    ship_coords = [(x + i, y) for i in range(size)]

                # Check if the ship overlaps with existing ships
                if any(self.grid[coord_x][coord_y] != "~" for coord_x, coord_y in ship_coords):
                    print("Ship overlaps with an existing ship. Try again.")
                    continue

                # Place the ship
                for coord_x, coord_y in ship_coords:
                    self.grid[coord_x][coord_y] = "S"
                self.ships.append(ship_coords)
                return True
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates and direction.")

    def manual_place_all_ships(self):
        """Allows manual placement of all ships."""
        for size in self.ship_sizes:
            self.display()  # Show the board after each ship placement
            if not self.manual_place_ship(size):
                raise RuntimeError("Unable to place all ships manually.")

    def receive_attack(self, x, y):
        """Handles an attack on the board."""
        if self.grid[x][y] == "S":
            self.grid[x][y] = "X"  # "X" represents a hit
            return True
        elif self.grid[x][y] == "~":
            self.grid[x][y] = "O"  # "O" represents a miss
            return False
        return None  # Already attacked

    def display(self, hide_ships=False):
        """Displays the board."""
        for row in self.grid:
            row_to_display = ["~" if hide_ships and cell == "S" else cell for cell in row]
            print(" ".join(row_to_display))

    def is_all_ships_destroyed(self):
        """Checks if all ships are destroyed."""
        for ship in self.ships:
            if any(self.grid[x][y] == "S" for x, y in ship):
                return False
        return True
