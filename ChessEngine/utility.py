from king import find_specific_king_pos
def check_move(start_pos: tuple, end_pos: tuple, moves_list: dict, player:str='w') -> bool:
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

def update_kings_and_rooks_moved(start_pos: tuple, end_pos: tuple,has_kings_moved, has_rooks_moved, player: str='w') -> list:
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
      



def is_in_check(current_board: dict, moves_list: dict, player: str):
    """
    The function `is_in_check` checks if a player is in check based on the current board state and
    possible moves of the opponent.
    
    :param current_board: The `current_board` parameter is a dictionary representing the current state
    of the chess board. It likely contains information about the positions of all pieces on the board
    :type current_board: dict
    :param moves_list: The `moves_list` parameter seems to be a dictionary where the keys are player
    colors ('w' or 'b') and the values are lists of possible moves for each player
    :type moves_list: dict
    :param player: The `player` parameter in the `is_in_check` function represents the player whose king
    we want to check for being in check. It can have a value of either 'b' for black player or 'w' for
    white player
    :type player: str
    :return: The function is checking if the opponent's moves list contains a move that puts the
    player's king in check. If such a move is found, the function returns True, indicating that the
    player is in check. Otherwise, it returns False, indicating that the player is not in check.
    """
    opponent = 'w' if player == 'b' else 'b'
    for mov in moves_list[opponent]:
        if mov[1] == find_specific_king_pos(current_board, player):
            return True
    return False
        
    