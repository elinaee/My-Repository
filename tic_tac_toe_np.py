# Tic-Tac-Toe program
# Author: Elisabete Bragança

import numpy as np
import time 

print("Hello there! Welcome to Tic-tac-toe! Get ready to play and have some fun with this classic game!")

time.sleep(4)

def main():
    player = play_turn()
    result = check_win()


grid = np.arange(1, 10).reshape(3,3)
row0 = grid[0]
row1 = grid[1]
row2 = grid[2]
column0 = grid[:, 0]
column1 = grid[:, 1]
column2 = grid[:, 2]


def check_win():
    if any(np.sum(grid, 1) == 3) or any(np.sum(grid, 0) == 3) or sum(np.diag(grid)) == 3 or sum(np.diag(grid [::-1])) == 3:
        return True
    if any(np.sum(grid, 1) == -3) or any(np.sum(grid, 0) == -3) or sum(np.diag(grid)) == -3 or sum(np.diag(grid [::-1])) == -3:
        return True
    return False


def play_turn():
    x = int(input(f"What is player {turn}'s x position ?"))
    o = int(input(f"What is player {turn}'s o position ?"))
    try:
        if grid[o, x] == 0:
            grid[o, x] = turn
        else:
            play_turn()
    except IndexError:
        play_turn()


turn = 1
move = 9

while move > 0:
    print(grid)
    play_turn()
    if check_win():
        print(f"Player {turn} has won!")
        break
    turn = turn * -1
    move = move -1

print("Thank you for playing! Hope you enjoyed!")

if __name__ == "__main__":
    main()