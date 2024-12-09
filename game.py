

from board import Board
from player import HumanPlayer, ComputerPlayer
from utils import print_divider

def main():
    board_size = 10

    # Create boards
    human_board = Board(board_size)
    computer_board = Board(board_size)

    # Create players
    human = HumanPlayer("You", human_board)
    computer = ComputerPlayer("Computer", computer_board)

    # Place ships
    print("Place your ships manually.")
    human.place_ships()
    print("\nComputer is placing its ships...")
    computer.place_ships()

    # Main game loop
    while True:
        print_divider()
        print("Your board:")
        human.board.display()

        print_divider()
        print("Computer's board (hidden):")
        computer.board.display(hide_ships=True)

        print_divider()
        print("Your turn:")
        hit = human.attack(computer.board)
        if hit:
            print("You hit a ship!")
        else:
            print("You missed!")

        if computer.board.is_all_ships_destroyed():
            print("Congratulations! You sunk all the computer's ships!")
            break

        print_divider()
        print("Computer's turn...")
        hit = computer.attack(human.board)
        if hit:
            print("The computer hit your ship!")
        else:
            print("The computer missed!")

        if human.board.is_all_ships_destroyed():
            print("Oh no! The computer sunk all your ships!")
            break

if __name__ == "__main__":
    main()
