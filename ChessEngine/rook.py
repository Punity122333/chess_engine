rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                            
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
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1]))))
                            
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].islower():
                            
                            check = False
                            chain += 1
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False
                        