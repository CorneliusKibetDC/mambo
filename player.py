
import random

class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def place_ships(self):
        """Default ship placement for a player."""
        self.board.place_all_ships()


class HumanPlayer(Player):
    def place_ships(self):
        """Allows the human player to place their ships manually."""
        print("Time to place your ships!")
        for size in self.board.ship_sizes:
            while True:
                try:
                    print(f"Placing a ship of size {size}")
                    coords = input(f"Enter starting coordinates (row col) for the ship of size {size}: ").split()
                    x, y = int(coords[0]), int(coords[1])
                    direction = input("Enter direction (h for horizontal, v for vertical): ").strip().lower()

                    if direction not in ['h', 'v']:
                        print("Invalid direction. Use 'h' for horizontal or 'v' for vertical.")
                        continue

                    # Generate ship coordinates based on direction
                    if direction == 'h':
                        if y + size > self.board.size:  # Ensure the ship fits horizontally
                            print("The ship doesn't fit horizontally. Try again.")
                            continue
                        coordinates = [(x, y + i) for i in range(size)]
                    else:  # vertical
                        if x + size > self.board.size:  # Ensure the ship fits vertically
                            print("The ship doesn't fit vertically. Try again.")
                            continue
                        coordinates = [(x + i, y) for i in range(size)]

                    # Validate that no existing ship overlaps with the new one
                    if all(self.board.grid[cx][cy] == "~" for cx, cy in coordinates):
                        for cx, cy in coordinates:
                            self.board.grid[cx][cy] = "S"
                        self.board.ships.append(coordinates)
                        break
                    else:
                        print("The ship overlaps with another ship. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please ensure coordinates are within bounds and try again.")

    def attack(self, opponent_board):
        """Allows the human player to attack the opponent's board."""
        while True:
            try:
                coords = input("Enter coordinates to attack (e.g., 2 3): ").split()
                x, y = int(coords[0]), int(coords[1])
                if 0 <= x < opponent_board.size and 0 <= y < opponent_board.size:
                    result = opponent_board.receive_attack(x, y)
                    if result is not None:
                        if result:
                            print(f"{self.name} hit a ship at ({x}, {y})!")
                        else:
                            print(f"{self.name} missed at ({x}, {y}).")
                        return result
                    else:
                        print("You already attacked this spot. Try again.")
                else:
                    print("Coordinates out of bounds. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter coordinates as two integers separated by a space.")


class ComputerPlayer(Player):
    def attack(self, opponent_board):
        """Allows the computer to attack the opponent's board."""
        while True:
            x, y = random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)
            result = opponent_board.receive_attack(x, y)
            if result is not None:
                if result:
                    print(f"{self.name} hit a ship at ({x}, {y})!")
                else:
                    print(f"{self.name} missed at ({x}, {y}).")
                return result
