rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
queen_offsets = rook_offsets + bishop_offsets

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
                            
                        if (k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1]) in current_board and current_board[(k[0] + chain * offset[0] - offset[0], k[1] + chain * offset[1] - offset[1])].islower():
                            
                            check = False
                            chain += 1
                            moves_list['b'].append((k, (k[0] + (chain * offset[0] - offset[0] - offset[0]), k[1] + (chain * offset[1] - offset[1] - offset[1]))))
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