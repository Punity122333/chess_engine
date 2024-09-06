from utility import is_in_check, is_attacking

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
    opponent = 'w' if player == 'b' else 'b'
    if current_board[(5,7)] == '' and current_board[(6,7)] == '' and has_kings_moved[0] == 0 and has_rooks_moved[1] == 0 and player == 'w' and current_board[(7,7)] == 'r':
        if not is_in_check(current_board, moves_list, player) and not is_attacking(moves_list, opponent, (5,7)) and not is_attacking(moves_list, opponent, (6,7)):
            moves_list[player].append(((4,7),(6,7)))
            castles.append(((4,7),(6,7)))
    if current_board[(5,0)] == '' and current_board[(6,0)] == '' and has_kings_moved[1] == 0 and has_rooks_moved[3] == 0 and player == 'b' and current_board[(7,0)] == 'R':
        if not is_in_check(current_board, moves_list, player) and not is_attacking(moves_list, opponent, (5,0)) and not is_attacking(moves_list, opponent, (6,0)):
            moves_list[player].append(((4,0),(6,0)))
            castles.append(((4,0),(6,0)))
    if current_board[(3,7)] == '' and current_board[(2,7)] == '' and current_board[(1,7)] == '' and has_kings_moved[0] == 0 and has_rooks_moved[0] == 0 and player == 'w' and current_board[(0,7)] == 'r':
        if not is_in_check(current_board, moves_list, player) and not is_attacking(moves_list, opponent, (3,7)) and not is_attacking(moves_list, opponent, (2,7)) and not is_attacking(moves_list, opponent, (1,7)):
            moves_list[player].append(((4,7),(2,7)))
            castles.append(((4,7),(2,7)))
    if current_board[(3,0)] == '' and current_board[(2,0)] == '' and current_board[(1,0)] == '' and has_kings_moved[1] == 0 and has_rooks_moved[2] == 0 and player == 'b' and current_board[(0,0)] == 'R':
        if not is_in_check(current_board, moves_list, player) and not is_attacking(moves_list, opponent, (3,0)) and not is_attacking(moves_list, opponent, (2,0)) and not is_attacking(moves_list, opponent, (1,0)):
            moves_list[player].append(((4,0),(2,0)))
            castles.append(((4,0),(2,0)))
    
    return [castles, moves_list]