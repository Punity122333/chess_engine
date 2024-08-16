# The above code is defining the initial setup of a chessboard with the starting positions of the
# pieces for a game of chess. It initializes lists and dictionaries to represent the white and black
# pieces on the board, with their respective locations. The white pieces are represented by lowercase
# letters and the black pieces are represented by uppercase letters. The pieces include rooks,
# knights, bishops, queens, kings, and pawns.
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = {(0, 0):'R', (1, 0):u'N', (2, 0):u'B', (3, 0):u'Q', (4, 0):u'K', (5, 0):'B', (6, 0):u'N', (7, 0):u'R',
                   (0, 1):'P', (1, 1):'P', (2, 1):'P', (3, 1):'P', (4, 1):'P', (5, 1):'P', (6, 1):'P', (7, 1):'P'}
white_locations = {(0, 7):'r', (1, 7):'n', (2, 7):'b', (3, 7):u'q', (4, 7):u'k', (5, 7):'b', (6, 7):'n', (7, 7):'r',
                   (0, 6):'p', (1, 6):'p', (2, 6):'p', (3, 6):'p', (4, 6):'p', (5, 6):'p', (6, 6):'p', (7, 6):'p'}
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
board = {(i, j): '' for i in range(8) for j in range(8)}

knight_offets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
queen_offsets = rook_offsets + bishop_offsets
king_offsets = queen_offsets.copy()

for k, v in board.items():
    if k in white_locations:
        board[k] = white_locations[k]
    if k in black_locations:
        board[k] = black_locations[k]
moves_list = {'w':[],'b':[]}
alphdict = {'a':0,'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
revdict = {v: k for k, v in alphdict.items()}

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
            if k[0] > 0 and current_board[(k[0]-1, k[1]+1)] in ['p','n','b','r','q']:
                moves_list['b'].append((k, (k[0]-1, k[1]+1)))
            if k[0] < 7 and current_board[(k[0]+1, k[1]+1)] in ['p','n','b','r','q']:
                moves_list['b'].append((k, (k[0]+1, k[1]+1)))
        if v == 'p':
            if k[1] == 6 and current_board[(k[0], k[1]-1)] == '' and not current_board[(k[0], k[1]-1)].isupper():
                moves_list['w'].append((k, (k[0], k[1]-1)))
                if k[1] == 6 and current_board[(k[0], k[1]-2)] == '':
                    moves_list['w'].append((k, (k[0], k[1]-2)))
            if k[0] > 0 and current_board[(k[0]-1, k[1]-1)] in ['P','N','B','R','Q']:
                moves_list['w'].append((k, (k[0]-1, k[1]-1)))
            if k[0] < 7 and current_board[(k[0]+1, k[1]-1)] in ['P','N','B','R','Q']:
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
            
def check_rook(current_board: dict,moves_list: list, value="rook"):
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
                        if current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                        chain += 1
                        
                        if check:
                            moves_list['w'].append((k, (k[0], k[1] + (chain * offset[1] - 1)))) if offset[1] == 1 else moves_list['w'].append((k, (k[0] + (chain * offset[0] + 1), k[1])))
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
                        if current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                        chain += 1
                        
                        if check:
                            moves_list['b'].append((k, (k[0], k[1] + (chain * offset[1] - 1)))) if offset[1] == 1 else moves_list['b'].append((k, (k[0] + (chain * offset[0] + 1), k[1])))
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
        if v == "b":
            for offset in bishop_offsets:
                check = True
                chain = 1
                while check:
                    
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper() or current_board[(k[0] + \
                        chain * offset[0], k[1] + chain * offset[1])] == ""):
                        if current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].isupper():
                            check = False
                        chain += 1
                        
                        if check:
                            if offset == (1, -1):
                                moves_list['w'].append((k, (k[0] + (chain * offset[0] - 1), k[1] + (chain * offset[1] + 1))))
                            elif offset == (-1, -1):
                                
                                moves_list['w'].append((k, (k[0] + (chain * offset[0] + 1), k[1] + (chain * offset[1] + 1))))
                            elif offset == (-1, 1):
                                
                                moves_list['w'].append((k, (k[0] + (chain * offset[0] + 1), k[1] + (chain * offset[1] - 1))))
                            else:
                                moves_list['w'].append((k, (k[0] + (chain * offset[0] - 1), k[1] + (chain * offset[1] - 1))))
                            
                    else:
                        check = False
        chain = 1
        check = True
        if v == "B":
            for offset in bishop_offsets:
                check = True
                chain = 1
                while check:
                    
                    if (k[0] + chain * offset[0], k[1] + chain * offset[1]) in current_board and (current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower() or current_board[(k[0] + \
                        chain * offset[0], k[1] + chain * offset[1])] == ""):
                        if current_board[(k[0] + chain * offset[0], k[1] + chain * offset[1])].islower():
                            check = False
                        chain += 1
                        
                        if check:
                            if offset == (1, -1):
                                moves_list['b'].append((k, (k[0] + (chain * offset[0] - 1), k[1] + (chain * offset[1] + 1))))
                            elif offset == (-1, -1):
                                
                                moves_list['b'].append((k, (k[0] + (chain * offset[0] + 1), k[1] + (chain * offset[1] + 1))))
                            elif offset == (-1, 1):
                                
                                moves_list['b'].append((k, (k[0] + (chain * offset[0] + 1), k[1] + (chain * offset[1] - 1))))
                            else:
                                moves_list['b'].append((k, (k[0] + (chain * offset[0] - 1), k[1] + (chain * offset[1] - 1))))
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
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
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
    for k, v in current_board.items():
        if v == "k":
            for offset in king_offsets:
                if (k[0] + offset[0], k[1] + offset[1]) in current_board and (current_board[(k[0] + offset[0], k[1] + offset[1])].isupper() or current_board[(k[0] + offset[0], k[1] + offset[1])] == ""):
                    moves_list['w'].append((k, (k[0] + offset[0], k[1] + offset[1])))
        if v == "K":
            for offset in king_offsets:
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
            print(f'{board[(j, i)] if board[(j, i)] else " "} |',end= " ")
        print("\n+---+---+---+---+---+---+---+---+\n|",end=" ") if i != 7 else print("\n+---+---+---+---+---+---+---+---+")
    print()    
    
def make_move(start_pos: tuple, end_pos: tuple,current_board : dict,player:str='w'):
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
        piece = current_board[start_pos]
        current_board[start_pos] = ''
        current_board[end_pos] = piece
    else:
        print(start_pos, "to", end_pos, "is not a valid move!")
        print("Move not possible!")
        
def check_check(current_board: dict, player: str='w', moves_list = moves_list):
    """
    This function checks if the opponent's king is in check on the current board for a given player.
    
    :param current_board: The function `check_check` seems to be checking if the opponent's king is in
    check based on the current board state and the possible moves for the player. However, there are a
    few issues in the code snippet you provided:
    :type current_board: dict
    :param player: The `player` parameter in the `check_check` function represents the current player
    whose turn it is to move. By default, it is set to 'w' (white player). The function checks if the
    opponent's king is in check by iterating through the current board state and looking for possible
    moves, defaults to w
    :type player: str (optional)
    :param moves_list: It seems like the definition of `moves_list` is missing from the provided code
    snippet. Could you please provide the definition of `moves_list` so that I can assist you further
    with the `check_check` function?
    :return: a boolean value - True if the opponent's king is in check, and False if it is not in check.
    """
    check_moves = []
    player2 = 'b' if player == 'w' else 'w'
    for k, v in current_board.items():
        if player2 == 'b' and v == 'K':
            king_pos = k
            for move in moves_list[player]:
                if move[1] == king_pos:
                    return True
            
        elif player2 == 'w' and v == 'k':
            king_pos = k
            for move in moves_list[player]:
                if move[1] == king_pos:
                    return True
    return False

def find_king_pos(current_board: dict, player: str) -> tuple:
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
    for k,v in current_board.items():
        if player == 'w' and v == 'k':
            king_pos = k
        if player == 'b' and v == 'K':
            king_pos = k
    return king_pos
        
                    
def remove_illegal_moves(current_board: dict, moves_list: dict, player: str) -> dict:
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
    print(king_pos)
    opponent = 'w' if player == 'b' else 'b'
    deleted_moves = []
    for mov in moves_list_copy[player]:
        current_board2 = current_board.copy()
        moves_list2 = {'w':[], 'b':[]}
        
        make_move(mov[0], mov[1], current_board2, player)
        check_bishop(current_board2, moves_list2)
        check_knight(current_board2, moves_list2)
        check_king(current_board2, moves_list2)
        check_queen(current_board2, moves_list2)
        check_rook(current_board2, moves_list2)
        check_pawn(current_board2, moves_list2)
        
        for mov2 in moves_list2[opponent]:
            
            if mov2[1] == king_pos:
                deleted_moves.append(mov)
                
    
    for mov in deleted_moves:
        moves_list_copy[player].remove(mov)
    return moves_list_copy
                
        
    
    
def check_move(start_pos: tuple, end_pos: tuple, player:str='w'):
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
        
player = 'w'
board2 = board.copy()
check_bishop(board, moves_list)
check_knight(board, moves_list)
check_pawn(board, moves_list)
check_rook(board, moves_list)
check_queen(board, moves_list)
check_king(board, moves_list)

# Game Loop

while True:
    print_board()
    
    print("White's turn!",end=" ") if player == 'w' else print("Black's turn!",end=" ")
    print("Enter your move (e.g e2e4):")
    
    
    move = list(input().split(', '))
    if move[0] == 'quit':
        break
    move = parse_move('.'.join(move))
    
    
    
    
    if not check_move(move[0], move[1], player):
        print("Move not possible!")
        continue
    make_move(move[0], move[1], board, player)
    check_bishop(board, moves_list)
    check_knight(board, moves_list)
    check_pawn(board, moves_list)
    check_rook(board, moves_list)
    check_queen(board, moves_list)
    check_king(board, moves_list)
    opponent = 'w' if player == 'b' else 'b'
    moves_list = remove_illegal_moves(board, moves_list, opponent)
    
    
    player = 'b' if player == 'w' else 'w'
    
    
    
        