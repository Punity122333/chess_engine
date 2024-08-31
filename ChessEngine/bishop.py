bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

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
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
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
                            moves_list['w'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
                    else:
                        check = False