from offsets import *
from pawn import check_pawn
from parsing import parse_move
from knight import check_knight
from rook import check_rook
from bishop import check_bishop
from queen import check_queen
from king import check_king, find_king_pos, find_specific_king_pos
from move import make_move

def remove_illegal_moves(current_board: dict, moves_list: dict, can_passant: list, castles: list, player: str) -> dict:
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
   
    opponent = 'w' if player == 'b' else 'b'
    deleted_moves = []
    for mov in moves_list_copy[player]:
        if mov in castles:
            continue
        current_board2 = current_board.copy()
        moves_list2 = {'w':[], 'b':[]}
        
        make_move(mov[0], mov[1], current_board2, can_passant, castles, moves_list, player, check_promotion = False)
        check_bishop(current_board2, moves_list2)
        check_knight(current_board2, moves_list2)
        check_king(current_board2, moves_list2)
        check_queen(current_board2, moves_list2)
        check_rook(current_board2, moves_list2)
        check_pawn(current_board2, moves_list2)
        
        for mov2 in moves_list2[opponent]:
            
            if mov2[1] == find_specific_king_pos(current_board2, player):
                deleted_moves.append(mov)
    
    for mov in moves_list[player]:
        if player == 'w' and current_board[mov[1]].islower():
            deleted_moves.append(mov)
        if player == 'b' and current_board[mov[1]].isupper():
            deleted_moves.append(mov)
        
    for mov in deleted_moves:
        if mov in moves_list_copy[player]:
            moves_list_copy[player].remove(mov)
    
                
    opponent = 'w' if player == 'b' else 'b'
    
    moves_list_copy2 = {'w':[],'b':[]}
    check_bishop(current_board, moves_list_copy2)
    check_knight(current_board, moves_list_copy2)
    check_pawn(current_board, moves_list_copy2)
    check_rook(current_board, moves_list_copy2)
    check_queen(current_board, moves_list_copy2)
    check_king(current_board, moves_list_copy2)   
    for mov in moves_list_copy[player]:
        if mov not in moves_list_copy2[player] and not (mov[0] in king_pos or mov[1] in king_pos):
            moves_list_copy[player].remove(mov)
    
    return moves_list_copy