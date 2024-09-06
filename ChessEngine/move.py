from termcolor import colored 
    
def make_move(start_pos: tuple, end_pos: tuple,current_board : dict,can_passant: list, castles: list, moves_list: dict, player:str='w',check_promotion=True):
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
           
                if current_board[start_pos] == 'p' and player ==  'w' and end_pos[1] == 0:
                    piec = 'q'
                elif current_board[start_pos] == 'P' and player == 'b' and end_pos[1] == 7:
                    piec = 'Q'
                else:
                    piec = current_board[start_pos]
                
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
        