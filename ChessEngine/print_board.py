from termcolor import colored

def print_board(board: dict):
    """
    The function `print_board` prints out a visual representation of a game board with 8 rows and
    columns.
    """
    print()
    print("+---+---+---+---+---+---+---+---+")
    print("| ",end="")
    for i in range(8):
        for j in range(8):
            if board[(j, i)].isupper():
                print(colored(f'{board[(j, i)] if board[(j, i)] else " " }',"cyan"),end= " ")
                print("|",end=" ")
            elif board[(j, i)].islower():
                print(colored(f'{board[(j, i)] if board[(j, i)] else " "}',"light_red"),end= " ")
                print("|",end=" ")
            else:
                print("  |",end=" ")
        print("\n+---+---+---+---+---+---+---+---+\n|",end=" ") if i != 7 else print("\n+---+---+---+---+---+---+---+---+")
    print()    
