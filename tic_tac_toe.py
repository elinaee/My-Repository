
# Tic-Tac-Toe program
# Author: Elisabete

import time

print("Hello there! Welcome to Tic-tac-toe! Get ready to play and have some fun with this classic game!")

time.sleep(4)

grid = {"1": " " , "2": " " , "3": " " ,
            "4": " " , "5": " " , "6": " " ,
            "7": " " , "8": " " , "9": " " }

grid_keys = []

for key in grid:
    grid_keys.append(key)


def printgrid(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


def main():

    turn = "X"
    count = 0


    for i in range(10):
        printgrid(grid)
        print("It's your turn," + turn + ". Please type the number of the place you would like to mark.")

        move = input()        

        if grid[move] == " ":
            grid[move] = turn
            count += 1
        else:
            print("That place is already filled.\n Please choose a different one.")
            continue

        # check if player X or O has won - every move after 5 moves. 
        if count >= 5:
            if grid["1"] == grid["2"] == grid["3"] != " ": # across the top
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")                
                break
            elif grid["4"] == grid["5"] == grid["6"] != " ": # across the middle
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break
            elif grid["7"] == grid["8"] == grid["9"] != " ": # across the bottom
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break
            elif grid["1"] == grid["4"] == grid["7"] != " ": # down the left side
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break
            elif grid["2"] == grid["5"] == grid["8"] != " ": # down the middle
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break
            elif grid["3"] == grid["6"] == grid["9"] != " ": # down the right side
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break 
            elif grid["7"] == grid["5"] == grid["3"] != " ": # diagonal
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break
            elif grid["1"] == grid["5"] == grid["9"] != " ": # diagonal
                printgrid(grid)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won! ****")
                break 

        # If neither X nor O wins and the grid is full, it's considered a draw/'tie'.
        if count == 9:
            print("\nGame Over!\n")                
            print("It's a Tie!!!")

        # switch between players after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Ask if the player wants to play again.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in grid_keys:
            grid[key] = " "

        main()

if __name__ == "__main__":
    main()