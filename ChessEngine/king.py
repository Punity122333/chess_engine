rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
queen_offsets = rook_offsets + bishop_offsets
king_offsets = queen_offsets.copy()

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
                    
