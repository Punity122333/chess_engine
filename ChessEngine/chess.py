# Importing Modules

import os
from pawn import check_pawn
from knight import check_knight
from rook import check_rook
from bishop import check_bishop
from queen import check_queen
from king import check_king
from illegal_removal import remove_illegal_moves
from specialmoves import check_castling, check_en_passant
from utility import is_in_check
from ui import gen_ui, render_checkmate, render_stalemate, render_repitition_stalemate, render_two_kings_stalemate, render_fifty_move_stalemate
from parsing import parse_move
import pygame
import time

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()
FPS = 30

# The above code is defining the initial setup of a chessboard with the starting positions of the
# pieces for a game of chess. It initializes lists and dictionaries to represent the white and black
# pieces on the board, with their respective locations. The white pieces are represented by lowercase
# letters and the black pieces are represented by uppercase letters. The pieces include rooks,
# knights, bishops, queens, kings, and pawns.
white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = {(0, 0):'R', (1, 0):'N', (2, 0):'B', (3, 0):'Q', (4, 0):'K', (5, 0):'B', (6, 0):'N', (7, 0):'R',
                   (0, 1):'P', (1, 1):'P', (2, 1):'P', (3, 1):'P', (4, 1):'P', (5, 1):'P', (6, 1):'P', (7, 1):'P'}
white_locations = {(0, 7):'r', (1, 7):'n', (2, 7):'b', (3, 7):'q', (4, 7):'k', (5, 7):'b', (6, 7):'n', (7, 7):'r',
                   (0, 6):'p', (1, 6):'p', (2, 6):'p', (3, 6):'p', (4, 6):'p', (5, 6):'p', (6, 6):'p', (7, 6):'p'}
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

# Castling flags

has_kings_moved = [0, 0]
has_rooks_moved = [0, 0, 0, 0]


piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
board = {(i, j): '' for i in range(8) for j in range(8)}

# The below Python code defines lists of offsets for different chess pieces. 
# - `knight_offsets` contains the possible moves for a knight on a chessboard.
# - `rook_offsets` contains the possible moves for a rook on a chessboard.
# - `bishop_offsets` contains the possible moves for a bishop on a chessboard.
# - `queen_offsets` contains the possible moves for a queen on a chessboard, which are a combination
# of rook and bishop moves.
# - `king_offsets` contains the possible moves for a king on a chessboard, which are the same as queen
# moves
knight_offets = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
rook_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bishop_offsets = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
queen_offsets = rook_offsets + bishop_offsets
king_offsets = queen_offsets.copy()

dragging = False
dragged_piece = None
dragged_pos = (0, 0)
# The code is iterating over the items in the `board` dictionary. For each key-value pair in the
# dictionary, it checks if the key is present in the `white_locations` dictionary. If it is, it
# updates the value in the `board` dictionary with the corresponding value from `white_locations`.
# Similarly, it checks if the key is present in the `black_locations` dictionary and updates the value
# in the `board` dictionary with the corresponding value from `black_locations` if it is.

for k, v in board.items():
    if k in white_locations:
        board[k] = white_locations[k]
    if k in black_locations:
        board[k] = black_locations[k]

        
moves_list = {'w':[],'b':[]}
alphdict = {'a':0,'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
revdict = {v: k for k, v in alphdict.items()}
prev_moves_list = {'w':[],'b':[]}
 
player = 'w'
prev_board = board.copy()
check_bishop(board, moves_list)
check_knight(board, moves_list)
check_pawn(board, moves_list)
check_rook(board, moves_list)
check_queen(board, moves_list)
check_king(board, moves_list)
can_passant, moves_list =  check_en_passant(board, prev_board, moves_list, player)[0], check_en_passant(board, prev_board, moves_list, player)[1]
castles, moves_list = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[0], check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[1]
os.system("cls")

# Game Loop

dragging = False
dragged_piece = None
dragged_pos = None
moves_hist = []
pieces_moved = []
piece = ''
font = pygame.font.Font('freesansbold.ttf', 32)
while True:
    #try:
        
        opponent = 'b' if player == 'w' else 'w'
        
        
        prev_moves_list = moves_list.copy()
        prev_board = board.copy()
        
        opponent = 'w' if player == 'b' else 'b'
        ls = gen_ui(['e2e4','e7e5'],board, moves_list[player], moves_list,  player, can_passant, castles,  window, moves_hist, pieces_moved, True, dragging, dragged_piece, dragged_pos, piece)
        
        dragging = ls[0]
        dragged_piece = ls[1]
        dragged_pos = ls[2]
        piece = ls[3]
        moves_hist = ls[4]
        pieces_moved = ls[5]
        if prev_board != board:
            check_bishop(board, moves_list)
            check_knight(board, moves_list)
            check_pawn(board, moves_list)
            check_rook(board, moves_list)
            check_queen(board, moves_list)
            check_king(board, moves_list)
            #has_kings_moved, has_rooks_moved = update_kings_and_rooks_moved(move[0], move[1], has_kings_moved, has_rooks_moved, player)[0], update_kings_and_rooks_moved(move[0], move[1], has_kings_moved, has_rooks_moved, player)[1]
            can_passant, moves_list =  check_en_passant(board, prev_board, moves_list, opponent)[0], check_en_passant(board, prev_board, moves_list, opponent)[1]
            castles, moves_list = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[0], check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player)[1]
            
            
            
            moves_list = remove_illegal_moves(board, moves_list, can_passant, castles, player)
            
        
        
            moves_list = remove_illegal_moves(board, moves_list, can_passant, castles, opponent)
            
        moves_list[opponent] = list(set(moves_list[opponent]))
        moves_list[player] = list(set(moves_list[player]))
        pieces = ''.join(list(board.values())).lower().replace(" ", "")
        if 'r' not in pieces and 'b' not in pieces and 'q' not in pieces and 'n' not in pieces and 'p' not in pieces:
            render_two_kings_stalemate(window)
            time.sleep(5)
            break
        
        if len(pieces_moved) > 100:
            render_fifty_move_stalemate(window)
            time.sleep(5)
            break
        if moves_list[player] == []:
            if is_in_check(board, moves_list, player):
                render_checkmate(window, player)
                time.sleep(5)
                break
            else:
                render_stalemate(window, player)
                time.sleep(5)
                break
        
        if len(moves_hist) > 6:
            render_repitition_stalemate(window)
            time.sleep(5)
            break
        
        
        
        if prev_board != board:
            
            player = 'b' if player == 'w' else 'w'
        
            
        
    #except Exception as e:
        #os.system("cls")
        #print(colored(f"An error occurred: {e}", "red"))
    

        