# Importing Modules

from termcolor import colored
import os

# The above code is defining the initial setup of a chessboard with the starting positions of the
# pieces for a game of chess. It initializes lists and dictionaries to represent the white and black
# pieces on the board, with their respective locations. The white pieces are represented by lowercase
# letters and the black pieces are represented by uppercase letters. The pieces include rooks,
# knights, bishops, queens, kings, and pawns.
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = {(0, 0):'', (1, 0):u'N', (2, 0):u'B', (3, 0):u'Q', (4, 0):u'K', (5, 0):'B', (6, 0):u'N', (7, 0):u'R',
                   (0, 1):'', (1, 1):'P', (2, 1):'P', (3, 1):'P', (4, 1):'P', (5, 1):'P', (6, 1):'P', (7, 1):'P'}
white_locations = {(0, 7):'r', (1, 7):'n', (2, 7):'b', (3, 7):u'q', (4, 7):u'k', (5, 7):'b', (6, 7):'n', (7, 7):'r',
                   (0, 6):'p', (1, 6):'p', (2, 6):'p', (3, 6):'p', (4, 6):'p', (5, 6):'p', (6, 6):'p', (7, 6):'p'}
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

# Castling flags

has_kings_moved = [0, 0]
has_rooks_moved = [0, 0, 0, 0]


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
board = {(i, j): '' for i in range(8) for j in range(8)}

# The below Python code defines lists of offsets for different chess pieces. 
# - `knight_offsets` contains the possible moves for a knight on a chessboard.
# - `rook_offsets` contains the possible moves for a rook on a chessboard.
# - `bishop_offsets` contains the possible moves for a bishop on a chessboard.
# - `queen_offsets` contains the possible moves for a queen on a chessboard, which are a combination
# of rook and bishop moves.
# - `king_offsets` contains the possible moves for a king on a chessboard, which are the same as queen
# moves
knight_offets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
queen_offsets = rook_offsets + bishop_offsets
king_offsets = queen_offsets.copy()


# The code is iterating over the items in the `board` dictionary. For each key-value pair in the
# dictionary, it checks if the key is present in the `white_locations` dictionary. If it is, it
# updates the value in the `board` dictionary with the corresponding value from `white_locations`.
# Similarly, it checks if the key is present in the `black_locations` dictionary and updates the value
# in the `board` dictionary with the corresponding value from `black_locations` if it is.

for k, v in board.items():
    if k in white_locations:
        board[k] = white_locations[k]
    if k in black_locations:
        board[k] = black_locations[k]
        
moves_list = {'w':[],'b':[]}
alphdict = {'a':0,'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
revdict = {v: k for k, v in alphdict.items()}
prev_moves_list = {'w':[],'b':[]}

def parse_coordinate(coord: str) -> tuple:
    """
    The function `parse_coordinate` takes a string representing a chess coordinate and returns a tuple
    with the corresponding numerical coordinates.
    
    :param coord: The `coord` parameter is a string representing a coordinate on a chess board. It
    typically consists of a letter (from 'a' to 'h') representing the column and a number (from 1 to 8)
    representing the row
    :type coord: str
    :return: The function `parse_coordinate` takes a string `coord` as input, which represents a chess
    coordinate in the format "letternumber" (e.g., "a1", "h8"). The function then returns a tuple
    containing the corresponding numerical coordinates in the format (x, y), where x represents the
    column (0-7) and y represents the row (0-7) on a
    """
    return (alphdict[coord[0]], 7 - (int(coord[1]) - 1))

def parse_move(mov: str) -> tuple:
    """
    The function `parse_move` takes a string representing a chess move and returns a tuple of the
    starting and ending coordinates of the move after parsing.
    
    :param mov: The `mov` parameter is a string representing a chess move. It consists of four
    characters where the first two characters represent the starting position of a piece on a
    chessboard, and the last two characters represent the ending position of the piece after the move
    :type mov: str
    :return: The `parse_move` function is returning a tuple containing the start and end coordinates of
    a move.
    """
    
    mov = list(mov  )
    start = parse_coordinate(mov[0] +mov[1])
    end = parse_coordinate(mov[2] + mov[3])
    return (start, end)
    

    
def check_pawn(current_board:dict, moves_list: list):
    """
    The function `check_pawn` checks for possible moves for pawns on a chess board based on the current
    board configuration.
    
    :param current_board: The function `check_pawn` seems to be checking the possible moves for pawns on
    a chess board based on the current board state. The `current_board` parameter is a dictionary
    representing the current state of the chess board. The keys of the dictionary are tuples
    representing the coordinates of each square on
    :type current_board: dict
    :param moves_list: The `moves_list` parameter in the `check_pawn` function is a dictionary that
    contains lists of possible moves for white ('w') and black ('b') pawns. The function checks the
    current board state to determine the valid moves for each pawn and appends them to the corresponding
    list in
    :type moves_list: list
    """
    for k, v in current_board.items():
        if v == 'P':
            if k[1] == 1 and current_board[(k[0], k[1]+1)] == '' and not current_board[(k[0], k[1]+1)].islower():
                moves_list['b'].append((k, (k[0], k[1]+1)))
                if k[1] == 1 and current_board[(k[0], k[1]+2)] == '':
                    
                    moves_list['b'].append((k, (k[0], k[1]+2)))
            if (k[0], k[1] + 1) in current_board and current_board[(k[0], k[1]+1)] == '' and not current_board[(k[0], k[1]+1)].islower():
                moves_list['b'].append((k, (k[0], k[1]+1)))
            if k[0] > 0 and (k[0]-1,k[1]+1) in current_board and current_board[(k[0]-1, k[1]+1)] in ['p','n','b','r','q','k']:
                moves_list['b'].append((k, (k[0]-1, k[1]+1)))
            if k[0] < 7 and (k[0]+1,k[1]+1) in current_board and current_board[(k[0]+1, k[1]+1)] in ['p','n','b','r','q','k']:
                moves_list['b'].append((k, (k[0]+1, k[1]+1)))
        if v == 'p':
            if k[1] == 6 and current_board[(k[0], k[1]-1)] == '' and not current_board[(k[0], k[1]-1)].isupper():
                moves_list['w'].append((k, (k[0], k[1]-1)))
                if k[1] == 6 and current_board[(k[0], k[1]-2)] == '':
                    
                    moves_list['w'].append((k, (k[0], k[1]-2)))
            if (k[0], k[1] - 1) in current_board and current_board[(k[0], k[1]-1)] == '' and not current_board[(k[0], k[1]-1)].islower():
                moves_list['w'].append((k, (k[0], k[1]-1)))
            if k[0] > 0 and (k[0]-1,k[1]-1) in current_board and current_board[(k[0]-1, k[1]-1)] in ['P','N','B','R','Q','K']:
                moves_list['w'].append((k, (k[0]-1, k[1]-1)))
            if k[0] < 7 and (k[0]+1,k[1]-1) in current_board and current_board[(k[0]+1, k[1]-1)] in ['P','N','B','R','Q','K']:
                moves_list['w'].append((k, (k[0]+1, k[1]-1)))
            

    
                
def check_knight(current_board: dict, moves_list: list):
    """
    The function `check_knight` iterates through a chess board to find valid knight moves for white and
    black knights.
    
    :param current_board: The function `check_knight` takes a current chess board represented as a
    dictionary where keys are positions on the board and values are the pieces at those positions, and a
    list of moves. It checks for valid knight moves on the board and appends them to the moves list
    :type current_board: dict
    :param moves_list: It seems like the definition of the `moves_list` parameter is missing in your
    code snippet. Could you please provide more information or context about the `moves_list` parameter
    so that I can assist you further with the `check_knight` function?
    :type moves_list: list
    """
    for k,v in current_board.items():
        if v == "N":
            for offset in knight_offets:
                if (k[0] + offset[0], k[1] + offset[1]) in current_board and (current_board[(k[0] + offset[0], k[1] + offset[1])].islower() or current_board[(k[0] + offset[0], k[1] + offset[1])] == ""):
                    moves_list['b'].append((k, (k[0] + offset[0], k[1] + offset[1])))
        if v == "n":
            for offset in knight_offets:
                if (k[0] + offset[0], k[1] + offset[1]) in current_board and (current_board[(k[0] + offset[0], k[1] + offset[1])].isupper() or current_board[(k[0] + offset[0], k[1] + offset[1])] == ""):
                    moves_list['w'].append((k, (k[0] + offset[0], k[1] + offset[1])))
            
def check_rook(current_board: dict ,moves_list: dict, value="rook"):
    """
    The function `check_rook` iterates through a chess board to find valid moves for rooks and updates a
    moves list accordingly.
    
    :param current_board: The function `check_rook` seems to be checking for valid moves for rooks on a
    chessboard based on the provided `current_board` dictionary. It appears to be iterating over the
    board positions and checking for possible rook moves in horizontal and vertical directions
    :type current_board: dict
    :param moves_list: The `moves_list` parameter in the `check_rook` function seems to be a dictionary
    that contains lists of moves for white ('w') and black ('b') players. The function appears to be
    checking for valid rook moves on a chessboard based on the current board state provided in the
    :type moves_list: list
    :param value: The `value` parameter in the `check_rook` function is used to specify the type of
    piece being checked for on the board. In this case, the function is checking for rooks (both
    lowercase 'r' and uppercase 'R') on the board. The default value for the `, defaults to rook
    (optional)
    """
    chain = 1
    check = True
    for k, v in current_board.items():
        check = True
        if v == "r":
            for offset in rook_offsets:
                check = True
                chain = 1
                while check:
                    
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper() or current_board[(k[0] + \
                        chain * offset[0], k[1] + chain * offset[1])] == ""):
                        
                        chain += 1
                        
                        if check:
                            moves_list['w'].append((k, (k[0], k[1] + (chain * offset[1] - 1)))) if offset[1] == 1 else moves_list['w'].append((k, (k[0] + (chain * offset[0] + 1), k[1])))
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].isupper():
                            
                            check = False
                            chain += 1
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False
        chain = 1
        check = True
        if v == "R":
            for offset in rook_offsets:
                check = True
                chain = 1
                while check:
                    
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower() or current_board[(k[0] + \
                        chain * offset[0], k[1] + chain * offset[1])] == ""):
                        
                        chain += 1
                        
                        if check:
                            
                            moves_list['b'].append((k, (k[0], k[1] + (chain * offset[1] - 1)))) if offset[1] == 1 else moves_list['b'].append((k, (k[0] + (chain * offset[0] + 1), k[1])))
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].islower():
                            
                            check = False
                            chain += 1
                            
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False
                    
def check_bishop(current_board: dict,moves_list: list, value="bishop"):
    """
    The function `check_bishop` iterates through a chess board to find valid moves for bishops and adds
    them to a list.
    
    :param current_board: The function `check_bishop` seems to be checking the possible moves for
    bishops on a chess board based on the current board state. It iterates over the board positions and
    checks for valid diagonal moves for both white ('w') and black ('b') bishops
    :type current_board: dict
    :param moves_list: The `moves_list` parameter is a dictionary that contains lists of moves for each
    player. The keys in the dictionary represent the player color ('w' for white and 'b' for black), and
    the values are lists of tuples representing the moves
    :type moves_list: list
    :param value: The `value` parameter in the `check_bishop` function is used to specify the type of
    piece being checked. In this case, the function is checking for bishops on the chessboard. The
    default value for `value` is set to "bishop", indicating that the function will check for bishops,
    defaults to bishop (optional)
    """
    chain = 1 
    check = True
    
    for k, v in current_board.items():
        check = True
        if v == "B":
            for offset in bishop_offsets:
                check = True
                chain = 1
                while check:
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower() or current_board[(k[0] + \
                            chain * offset[0], k[1] + chain * offset[1])] == ""):
                        if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper():
                            check = False
                            break
                            
                        chain += 1
                        
                        if check:
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                        if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                            chain += 1
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[1]), k[1] + (chain * offset[1] - offset[1]))))
                    else:
                        check = False
        if v == "b":
            for offset in bishop_offsets:
                check = True
                chain = 1
                while check:
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper() or current_board[(k[0] + \
                            chain * offset[0], k[1] + chain * offset[1])] == ""):
                        if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                            break
                        chain += 1
                        
                        if check:
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                            
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].isupper():
                            
                            check = False
                            chain += 1
                            if (k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))) == ((5,7),(2,4)):
                                raise RuntimeError("Error")
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False
                        
def check_queen(current_board: dict,moves_list: list ,value="queen"):
    """
    The function `check_queen` iterates through a chess board to find possible moves for queens and
    updates a list of moves accordingly.
    
    :param current_board: The function `check_queen` seems to be checking for possible moves of a queen
    on a chessboard based on the current board state. It iterates over the positions on the board and
    checks for possible moves in all directions for both white and black queens
    :type current_board: dict
    :param moves_list: The `moves_list` parameter is a dictionary that contains lists of moves for
    different pieces. In the function `check_queen`, it seems to be used to store the possible moves for
    the queen pieces on the chessboard. The keys `'b'` and `'w'` likely represent black and
    :type moves_list: list
    :param value: The `value` parameter in the `check_queen` function is used to specify the type of
    chess piece to check for. By default, it is set to "queen". This parameter allows the function to
    differentiate between checking for a white queen ("Q") and a black queen ("q") on, defaults to queen
    (optional)
    """
    chain = 1 
    check = True
    
    for k, v in current_board.items():
        check = True
        if v == "Q":
            for offset in queen_offsets:
                check = True
                chain = 1
                while check:
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower() or current_board[(k[0] + \
                            chain * offset[0], k[1] + chain * offset[1])] == ""):
                        
                        chain += 1
                        
                        if check:
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                        if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                            chain += 1
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[1]), k[1] + (chain * offset[1] - offset[1]))))
                    else:
                        check = False
        if v == "q":
            for offset in queen_offsets:
                check = True
                chain = 1
                while check:
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper() or current_board[(k[0] + \
                            chain * offset[0], k[1] + chain * offset[1])] == ""):
                        
                        chain += 1
                        
                        if check:
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                            
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].isupper():
                            
                            check = False
                            chain += 1
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False
                        
def check_king(current_board: dict, moves_list: list):
    """
    The function `check_king` iterates through a chess board to find legal moves for the white and black
    kings.
    
    :param current_board: The `current_board` parameter is a dictionary representing the current state
    of a chess board. The keys are tuples representing the coordinates of each square on the board, and
    the values are the pieces occupying those squares (e.g., "k" for black king, "K" for white king, etc
    :type current_board: dict
    :param moves_list: The `moves_list` parameter is a list that contains moves for each player. It is a
    dictionary where the keys are 'w' for white player and 'b' for black player. The values are lists of
    tuples representing the moves from one position to another on the chessboard
    :type moves_list: list
    """
    is_attacked = False
    for k, v in current_board.items():
        if v == "k":
            for offset in king_offsets:
                is_attacked = False
                if (k[0] + offset[0], k[1] + offset[1]) in current_board and (current_board[(k[0] + offset[0], k[1] + offset[1])].isupper() or current_board[(k[0] + offset[0], k[1] + offset[1])] == ""):
                    
                        moves_list['w'].append((k, (k[0] + offset[0], k[1] + offset[1])))
        if v == "K":
            for offset in king_offsets:
                is_attacked = False
                if (k[0] + offset[0], k[1] + offset[1]) in current_board and (current_board[(k[0] + offset[0], k[1] + offset[1])].islower() or current_board[(k[0] + offset[0], k[1] + offset[1])] == ""):
                    
                        moves_list['b'].append((k, (k[0] + offset[0], k[1] + offset[1])))
                    
    
            
                
def print_board():
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
    
def make_move(start_pos: tuple, end_pos: tuple,current_board : dict,can_passant: list, castles: list, player:str='w',check_promotion=True):
    """
    The function `make_move` takes the starting position, ending position, current board state, and
    player as input, and updates the board with the move if it is valid.
    
    :param start_pos: The `start_pos` parameter represents the current position of the piece on the
    board that you want to move. It is a tuple containing the coordinates (row, column) of the starting
    position of the piece
    :type start_pos: tuple
    :param end_pos: The `end_pos` parameter represents the position where the player wants to move their    
    piece to on the board. It is a tuple that contains the coordinates (row, column) of the destination
    position on the board
    :type end_pos: tuple
    :param current_board: The `current_board` parameter is a dictionary representing the current state
    of the game board. The keys in the dictionary are tuples representing the positions on the board,
    and the values are strings representing the pieces at those positions. For example,
    `current_board[(0, 0)]` would give you
    :type current_board: dict
    :param player: The `player` parameter in the `make_move` function represents the player who is
    making the move. It is a string that can have a value of either 'w' or 'b', indicating whether it is
    the white player or the black player making the move, defaults to w
    :type player: str (optional)
    """
    if (start_pos, end_pos) in moves_list[player]:
        
        if (start_pos, end_pos) in castles:
            if (start_pos, end_pos) == ((4, 7), (6, 7)):
                
                current_board[(5,7)] = 'r'
                current_board[(7,7)] = ''
            if (start_pos, end_pos) == ((4, 0), (6, 0)):
                current_board[(5,0)] = 'R'
                current_board[(7,0)] = ''
            if (start_pos, end_pos) == ((4, 7), (2, 7)):
                current_board[(3,7)] = 'r'
                current_board[(0,7)] = ''
            if (start_pos, end_pos) == ((4, 0), (2, 0)):
                current_board[(3, 0)] = 'R'
                current_board[(0, 0)] = ''
        if check_promotion:
            valid_promotion = False
            while not valid_promotion:
                if current_board[start_pos] == 'p' and player ==  'w' and end_pos[1] == 0:
                    piec = input(colored("Which piece do you want to promote to? ","cyan"))
                    piec = piec.lower()
                elif current_board[start_pos] == 'P' and player == 'b' and end_pos[1] == 7:
                    piec = input(colored("Which piece do you want to promote to? ", "cyan"))
                    piec = piec.upper()
                else:
                    piec = current_board[start_pos]
                if current_board[start_pos].lower() != 'p' or end_pos[1] not in (0, 7):
                    break
                if piec.lower() in 'rnqb' and current_board[start_pos].lower() == 'p' and end_pos[1] in (0,7):
                    valid_promotion = True
                else:
                    print(colored("Invalid promoting piece.","red"))
        else:
            piec = current_board[start_pos]
        
        current_board[start_pos] = ''
        current_board[end_pos] = piec
        if (start_pos, end_pos) in can_passant:
            if player == 'w':
                current_board[(end_pos[0],end_pos[1] + 1)] = ''
            if player == 'b':
                current_board[(end_pos[0],end_pos[1] - 1)] = ''
        
    else:
        print(start_pos, "to", end_pos, "is not a valid move!")
        print("Move not possible!")
        

def find_king_pos(current_board: dict, player: str) -> list:
    """
    The function `find_king_pos` searches a given chess board for the position of the king belonging to
    a specified player.
    
    :param current_board: The function `find_king_pos` takes two parameters:
    :type current_board: dict
    :param player: The `player` parameter in the `find_king_pos` function represents the player whose
    king position we are trying to find. It is a string that can have a value of either 'w' for white
    player or 'b' for black player
    :type player: str
    :return: The function `find_king_pos` returns the position of the king ('k' for white player or 'K'
    for black player) on the current board as a tuple.
    """
    poses = []
    for k,v in current_board.items():
        if player == 'w' and v == 'k':
            poses.append(k)
            for offset in king_offsets:
                poses.append((k[0] + offset[0], k[1] + offset[1])) if ((k[0] + offset[0], k[1] + offset[1]) in current_board and not current_board[(k[0] + offset[0], k[1] + offset[1])].islower()) else None
        if player == 'b' and v == 'K':
            poses.append(k)
            for offset in king_offsets:
                poses.append((k[0] + offset[0], k[1] + offset[1])) if ((k[0] + offset[0], k[1] + offset[1]) in current_board and not current_board[(k[0] + offset[0], k[1] + offset[1])].isupper()) else None
    return poses
        
def find_specific_king_pos(current_board: dict, player:str) -> tuple:
    for k, v in current_board.items():
        if player == 'b':
            if v == 'K':
                return k
        if player == 'w':
            if v == 'k':
                return k
                    
def remove_illegal_moves(current_board: dict, moves_list: dict, can_passant: list, castles: list, player: str) -> dict:
    """
    This Python function removes illegal moves for a player based on the current board state and
    available moves.
    
    :param current_board: The `current_board` parameter is a dictionary representing the current state
    of the chess board. It likely contains information about the positions of different pieces on the
    board
    :type current_board: dict
    :param moves_list: The `moves_list` parameter seems to be a dictionary containing moves for each
    player. The keys 'w' and 'b' likely represent the white and black players, respectively. The values
    are lists of moves that each player can make
    :type moves_list: dict
    :param player: The `player` parameter in the `remove_illegal_moves` function represents the current
    player whose moves are being checked for legality. It can have a value of either 'w' for white
    player or 'b' for black player
    :type player: str
    :return: The function `remove_illegal_moves` is returning a modified `moves_list_copy` dictionary
    with illegal moves removed for the specified player.
    """
    current_board2 = current_board.copy()
    moves_list_copy = moves_list.copy()
    moves_list2 = {'w':[], 'b':[]}
    king_pos = find_king_pos(current_board2, player)
   
    opponent = 'w' if player == 'b' else 'b'
    deleted_moves = []
    for mov in moves_list_copy[player]:
        if mov in castles:
            continue
        current_board2 = current_board.copy()
        moves_list2 = {'w':[], 'b':[]}
        
        make_move(mov[0], mov[1], current_board2, can_passant, castles, player, check_promotion = False)
        check_bishop(current_board2, moves_list2)
        check_knight(current_board2, moves_list2)
        check_king(current_board2, moves_list2)
        check_queen(current_board2, moves_list2)
        check_rook(current_board2, moves_list2)
        check_pawn(current_board2, moves_list2)
        
        for mov2 in moves_list2[opponent]:
            
            if mov2[1] == find_specific_king_pos(current_board2, player):
                deleted_moves.append(mov)
                
    for mov in moves_list[player]:
        if player == 'w' and current_board[mov[1]].islower():
            deleted_moves.append(mov)
        if player == 'b' and current_board[mov[1]].isupper():
            deleted_moves.append(mov)
        
    for mov in deleted_moves:
        if mov in moves_list_copy[player]:
            moves_list_copy[player].remove(mov)
    
                
    opponent = 'w' if player == 'b' else 'b'
    
    moves_list_copy2 = {'w':[],'b':[]}
    check_bishop(board, moves_list_copy2)
    check_knight(board, moves_list_copy2)
    check_pawn(board, moves_list_copy2)
    check_rook(board, moves_list_copy2)
    check_queen(board, moves_list_copy2)
    check_king(board, moves_list_copy2)   
    for mov in moves_list_copy[player]:
        if mov not in moves_list_copy2[player] and not (mov[0] in king_pos or mov[1] in king_pos):
            moves_list_copy[player].remove(mov)
    
    return moves_list_copy
                
def check_en_passant(current_board: dict, prev_board: dict, moves_list: dict, player: str) -> list:
    """
    This function `check_en_passant` checks for en passant moves in a chess game based on the
    current and previous board states.
    
    :param current_board: The function `check_en_passant` is designed to check for en passant moves in a
    chess game. It takes the current board state, the previous board state, a dictionary of moves, and
    the current player as input parameters
    :type current_board: dict
    :param prev_board: The `prev_board` parameter in the `check_en_passant` function represents the
    state of the chessboard before the current move is made. It is a dictionary that maps the
    coordinates of each square on the board to the piece occupying that square before the move
    :type prev_board: dict
    :param moves_list: The `moves_list` parameter in the `check_en_passant` function is a dictionary
    that stores the moves made by each player. It is structured as follows:
    :type moves_list: dict
    :param player: The `player` parameter in the `check_en_passant` function represents the current
    player making the move. It can be either 'w' for white or 'b' for black. The function checks for the
    en passant move possibility for the given player based on the current and previous board states
    :type player: str
    :return: The function `check_en_passant` is returning a list containing two elements: 
    1. The list `can_passant` which stores the possible en passant moves that can be made on the current
    board.
    2. The dictionary `moves_list` which contains the updated moves for the player after considering en
    passant moves.
    """
    can_passant = []
    
    if player == 'w':
        for k, v in current_board.items():
            if v == 'P' and k[1] == 3:
                   
                if prev_board[(k[0],k[1]-2)] == 'P':
                    
                    if (k[0] - 1, k[1]) in current_board and current_board[(k[0] - 1, k[1])] == 'p':
                        
                        moves_list[player].append(((k[0] - 1, k[1]),(k[0], k[1] - 1)))
                        can_passant.append(((k[0] - 1, k[1]),(k[0], k[1] - 1)))
                    if (k[0] + 1, k[1]) in current_board and current_board[(k[0] + 1, k[1])] == 'p':
                        
                        moves_list[player].append(((k[0] + 1, k[1]),(k[0], k[1] - 1)))
                        can_passant.append(((k[0] + 1, k[1]),(k[0], k[1] - 1)))
                        
    if player == 'b':
        for k, v in current_board.items():
            if v == 'p' and k[1] == 4:
                
                if prev_board[(k[0],k[1]+2)] == 'p':
                    
                    if (k[0] - 1, k[1]) in current_board and current_board[(k[0] - 1, k[1])] == 'P':
                        moves_list[player].append(((k[0] - 1, k[1]),(k[0], k[1] + 1)))
                        can_passant.append(((k[0] - 1, k[1]),(k[0], k[1] + 1)))
                    if (k[0] + 1, k[1]) in current_board and current_board[(k[0] + 1, k[1])] == 'P':
                        moves_list[player].append(((k[0] +  1, k[1]),(k[0], k[1] + 1)))
                        can_passant.append(((k[0] + 1, k[1]),(k[0], k[1] + 1)))
    return [can_passant, moves_list]
            
    
    
def check_move(start_pos: tuple, end_pos: tuple, player:str='w') -> bool:
    """
    The function `check_move` checks if a given move from `start_pos` to `end_pos` is valid for a
    specified player in a chess game.
    
    :param start_pos: The `start_pos` parameter represents the starting position of a piece on a
    chessboard. It is a tuple containing the coordinates (row, column) of the square where the piece is
    located before making a move
    :type start_pos: tuple
    :param end_pos: The `end_pos` parameter represents the final position where a player wants to move a
    piece on the board. It is a tuple that contains the coordinates (row, column) of the destination
    square on the board
    :type end_pos: tuple
    :param player: The `player` parameter in the `check_move` function represents the player who is
    making the move. It is a string that can have a value of either 'w' or 'b', indicating whether the
    player is white or black, respectively, defaults to w
    :type player: str (optional)
    :return: The function `check_move` is returning a boolean value indicating whether the move from
    `start_pos` to `end_pos` is valid for the specified player ('w' by default).
    """
    return (start_pos, end_pos) in moves_list[player]   

def update_kings_and_rooks_moved(start_pos: tuple, end_pos: tuple,player: str='w') -> list:
    """
    This Python function updates the status of kings and rooks based on their movement on a chessboard.
    
    :param start_pos: The `start_pos` parameter in the `update_kings_and_rooks_moved` function
    represents the starting position of a chess piece on the board. It is a tuple containing the
    coordinates (row, column) of the square where the piece is located before it moves
    :type start_pos: tuple
    :param end_pos: The `end_pos` parameter in the `update_kings_and_rooks_moved` function represents
    the ending position of a piece on a chessboard. It is a tuple containing the coordinates (row,
    column) where the piece will be moved to
    :type end_pos: tuple
    :param player: The `player` parameter in the `update_kings_and_rooks_moved` function represents the
    player whose move is being processed. It can have a value of either 'w' for white player or 'b' for
    black player. This parameter helps determine which player is making the move and accordingly,
    defaults to w
    :type player: str (optional)
    :return: The function `update_kings_and_rooks_moved` returns a list containing the updated values of
    `has_kings_moved` and `has_rooks_moved` after processing the given `start_pos`, `end_pos`, and
    `player` inputs.
    """
    if player == 'b' and has_rooks_moved[0] == 0 and end_pos == (0,7):
        has_rooks_moved[0] = -1
    if start_pos == (0, 7) and has_rooks_moved[0] == 0:
        has_rooks_moved[0] = 1
    if player == 'b' and has_rooks_moved[1] == 0 and end_pos == (7,7):
        has_rooks_moved[1] = -1
    if start_pos == (7, 7) and has_rooks_moved[1] == 0:
        has_rooks_moved[1] = 1
    if player == 'w' and has_rooks_moved[2] == 0 and end_pos == (0,0):
        has_rooks_moved[2] = -1
    if start_pos == (0, 0) and has_rooks_moved[2] == 0:
        has_rooks_moved[2] = 1
    if player == 'w' and has_rooks_moved[3] == 0 and end_pos == (7,0):
        has_rooks_moved[3] = -1
    if start_pos == (7, 0) and has_rooks_moved[3] == 0:
        has_rooks_moved[3] = 1
    if start_pos == (4,0):
        has_kings_moved[1] = 1
    if start_pos == (4,7):
        
        has_kings_moved[0] = 1
        
    return [has_kings_moved, has_rooks_moved]
      

def check_castling(current_board: dict, moves_list: dict, has_kings_moved: list, has_rooks_moved: list, player:str = 'w') -> list:
    """
    The function `check_castling` checks for valid castling moves in chess based on the current board
    position and piece movement history.
    
    :param current_board: The `check_castling` function you provided checks for valid castling moves in
    a chess game based on the current board position, the moves made so far, and whether the kings and
    rooks have moved. It then updates the moves list with the valid castling moves and returns the list
    of valid castling moves
    :type current_board: dict
    :param moves_list: The `moves_list` parameter in the `check_castling` function is a dictionary that
    stores the moves made by each player. It has the following structure:
    :type moves_list: dict
    :param has_kings_moved: The `has_kings_moved` parameter is a list that keeps track of whether the
    kings have moved in the game. It is a list containing two elements, where `has_kings_moved[0]`
    corresponds to the white king and `has_kings_moved[1]` corresponds to the black king
    :type has_kings_moved: list
    :param has_rooks_moved: The `has_rooks_moved` parameter is a list that keeps track of whether the
    rooks have moved for each player. It is used in the `check_castling` function to determine if
    castling is a valid move based on the current board position and the movement history of the rooks
    :type has_rooks_moved: list
    :param player: The `player` parameter in the `check_castling` function represents the current player
    making the move. It is a string parameter that can have a value of either 'w' (white player) or 'b'
    (black player) to indicate which player's turn it is, defaults to w
    :type player: str (optional)
    :return: The function `check_castling` returns a list containing two elements: the list of castling
    moves that are possible based on the current board state and the list of moves made so far for the
    player specified.
    """
    castles = []
    
    if current_board[(5,7)] == '' and current_board[(6,7)] == '' and has_kings_moved[0] == 0 and has_rooks_moved[1] == 0:
        moves_list[player].append(((4,7),(6,7)))
        castles.append(((4,7),(6,7)))
    if current_board[(5,0)] == '' and current_board[(6,0)] == '' and has_kings_moved[1] == 0 and has_rooks_moved[3] == 0:
        moves_list[player].append(((4,0),(6,0)))
        castles.append(((4,0),(6,0)))
    if current_board[(3,7)] == '' and current_board[(2,7)] == '' and current_board[(1,7)] == '' and has_kings_moved[0] == 0 and has_rooks_moved[0] == 0:
        moves_list[player].append(((4,7),(2,7)))
        castles.append(((4,7),(2,7)))
    if current_board[(3,0)] == '' and current_board[(2,0)] == '' and current_board[(1,0)] == '' and has_kings_moved[1] == 0 and has_rooks_moved[2] == 0:
        moves_list[player].append(((4,0),(2,0)))
        castles.append(((4,0),(2,0)))
    
    return [castles, moves_list]
    
player = 'w'
prev_board = board.copy()
check_bishop(board, moves_list)
check_knight(board, moves_list)
check_pawn(board, moves_list)
check_rook(board, moves_list)
check_queen(board, moves_list)
check_king(board, moves_list)
can_passant, moves_list =  check_en_passant(board, prev_board, moves_list, player)[0], check_en_passant(board, prev_board, moves_list, player)[1]
castles, moves_list = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[0], check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[1]
os.system("cls")

# Game Loop

while True:
    try:
        
        opponent = 'b' if player == 'w' else 'w'
        
        print_board()
        print("White's turn!",end=" ") if player == 'w' else print("Black's turn!",end=" ")
        print(colored("Enter your move (e.g e2e4):","yellow"))
        
        move = list(input().split(', '))
        if move[0] == 'quit':
            break
        move = parse_move('.'.join(move))
        
        if not check_move(move[0], move[1], player):
            os.system("cls")
            print(colored("Move not possible!","red"))
            continue
        prev_moves_list = moves_list.copy()
        prev_board = board.copy()
        make_move(move[0], move[1], board, can_passant, castles, player)
        opponent = 'w' if player == 'b' else 'b'
        os.system("cls")
        check_bishop(board, moves_list)
        check_knight(board, moves_list)
        check_pawn(board, moves_list)
        check_rook(board, moves_list)
        check_queen(board, moves_list)
        check_king(board, moves_list)
        has_kings_moved, has_rooks_moved = update_kings_and_rooks_moved(move[0], move[1], player)[0], update_kings_and_rooks_moved(move[0], move[1], player)[1]
        can_passant, moves_list =  check_en_passant(board, prev_board, moves_list, opponent)[0], check_en_passant(board, prev_board, moves_list, opponent)[1]
        castles, moves_list = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[0], check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[1]
        
        
        moves_list = remove_illegal_moves(board, moves_list, can_passant, castles, opponent)
        moves_list = remove_illegal_moves(board, moves_list, can_passant, castles, player)
        for mov in moves_list[opponent]:
            if opponent == 'w':
                if board[mov[0]].isupper():
                    moves_list[opponent].remove(mov)
            if opponent == 'b':
                if board[mov[0]].islower():
                    moves_list[opponent].remove(mov)
        
        moves_list[opponent] = list(set(moves_list[opponent]))
        moves_list[player] = list(set(moves_list[player]))
            
        if moves_list[opponent] == []:
            print_board()
            print(colored(f"White's king is in checkmate! Black wins!","light_green")) if opponent == 'w' else print(colored(f"Black's king is in checkmate! White wins!","light_green"))
            break

        player = 'b' if player == 'w' else 'w'
    except Exception as e:
        os.system("cls")
        print(colored(f"An error occurred: {e}", "red"))
    
print(colored("Thank you for playing chess!","light_cyan")) 
print()   

        
