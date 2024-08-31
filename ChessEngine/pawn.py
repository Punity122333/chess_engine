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