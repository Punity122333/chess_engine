knight_offets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

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