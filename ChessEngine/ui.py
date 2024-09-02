import pygame
import sys
from termcolor import colored
import os
import subprocess
from pawn import check_pawn
from parsing import parse_move
from knight import check_knight
from rook import check_rook
from bishop import check_bishop
from queen import check_queen
from king import check_king, find_king_pos, find_specific_king_pos
from move import make_move
from illegal_removal import remove_illegal_moves
from specialmoves import check_castling, check_en_passant
from print_board import print_board
from utility import check_move, update_kings_and_rooks_moved, is_in_check


white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = {(0, 0):'R', (1, 0):'N', (2, 0):'B', (3, 0):'Q', (4, 0):'K', (5, 0):'B', (6, 0):'N', (7, 0):'R',
                   (0, 1):'P', (1, 1):'P', (2, 1):'P', (3, 1):'P', (4, 1):'P', (5, 1):'P', (6, 1):'P', (7, 1):'P'}
white_locations = {(0, 7):'r', (1, 7):'n', (2, 7):'b', (3, 7):'q', (4, 7):'k', (5, 7):'b', (6, 7):'n', (7, 7):'r',
                   (0, 6):'p', (1, 6):'p', (2, 6):'p', (3, 6):'p', (4, 6):'p', (5, 6):'p', (6, 6):'p', (7, 6):'p'}
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
board = {(i, j): '' for i in range(8) for j in range(8)}
for k, v in board.items():
    if k in white_locations:
        board[k] = white_locations[k]
    if k in black_locations:
        board[k] = black_locations[k]
        
window = pygame.display.set_mode((800,800))
def blit_pieces(current_board: dict, image: pygame.image, window: pygame.display, moves: list, dragging: bool = False, dragged_piece = None):
    window_size = 800
    square_size = window_size // 8
    image_size = window_size // 8 - 10
    # Define the area to crop (x, y, width, height)
    crop_rect_king_w = pygame.Rect(5,5, 120,120)
    crop_rect_queen_w = pygame.Rect(138,5,120,120)
    crop_rect_pawn_w = pygame.Rect(670,5,120,120)
    crop_rect_rook_w = pygame.Rect(537,5,120,120)
    crop_rect_bishop_w = pygame.Rect(271,5,120,120)
    crop_rect_knight_w = pygame.Rect(404,5,120,120)
    crop_rect_king_b = pygame.Rect(5,140,120,120)
    crop_rect_queen_b = pygame.Rect(138,140,120,120)
    crop_rect_pawn_b = pygame.Rect(670,140,120,120)
    crop_rect_rook_b = pygame.Rect(537,140,120,120)
    crop_rect_knight_b = pygame.Rect(404,140,120,120)
    crop_rect_bishop_b = pygame.Rect(271,140,120,120)
    
    # Crop the image
    king_w = image.subsurface(crop_rect_king_w)
    king_w = pygame.transform.scale(king_w, (image_size, image_size))
    queen_w = image.subsurface(crop_rect_queen_w)
    queen_w = pygame.transform.scale(queen_w, (image_size, image_size))
    pawn_w = image.subsurface(crop_rect_pawn_w)
    pawn_w = pygame.transform.scale(pawn_w, (image_size, image_size))
    rook_w = image.subsurface(crop_rect_rook_w)
    rook_w = pygame.transform.scale(rook_w, (image_size, image_size))
    bishop_w = image.subsurface(crop_rect_bishop_w)
    bishop_w = pygame.transform.scale(bishop_w, (image_size, image_size))
    knight_w = image.subsurface(crop_rect_knight_w)
    knight_w = pygame.transform.scale(knight_w, (image_size, image_size))
    king_b = image.subsurface(crop_rect_king_b)
    king_b = pygame.transform.scale(king_b, (image_size, image_size))
    queen_b = image.subsurface(crop_rect_queen_b)
    queen_b = pygame.transform.scale(queen_b, (image_size, image_size))
    pawn_b = image.subsurface(crop_rect_pawn_b)
    pawn_b = pygame.transform.scale(pawn_b, (image_size, image_size))
    rook_b = image.subsurface(crop_rect_rook_b)
    rook_b = pygame.transform.scale(rook_b, (image_size, image_size))
    knight_b = image.subsurface(crop_rect_knight_b)
    knight_b = pygame.transform.scale(knight_b, (image_size, image_size))
    bishop_b = image.subsurface(crop_rect_bishop_b)
    bishop_b = pygame.transform.scale(bishop_b, (image_size, image_size))
    
    imgdict = dict(K=king_b, B=bishop_b, N=knight_b, R=rook_b, P=pawn_b, Q=queen_b, k=king_w, b=bishop_w, r=rook_w, q=queen_w, n=knight_w, p=pawn_w)
    
    
    for k,v in current_board.items():
        
        window.blit(imgdict[v],((k[0] * square_size) + 5, (k[1] * square_size) + 5)) if v in imgdict else None
    
    if dragging:
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        square_x , square_y = mouse_x // square_size, mouse_y // square_size
        with open("dragposes.txt","r") as file:
            data = file.read()
            data = data.strip("\n")
            move = (int(data[0]),int(data[1]))
        for mov in moves:
            if mov[0] == move:
                pygame.draw.rect(window, (210,60,60), (mov[1][0]*square_size, mov[1][1]*square_size, square_size, square_size))
        pygame.draw.rect(window, (240, 0, 0), (move[0]*square_size, move[1]*square_size, square_size, square_size))
        
        window.blit(imgdict[dragged_piece], (mouse_x - 50, mouse_y - 50))

def gen_ui(current_board: dict, moves: list, player, window, dragging = False, dragged_piece = None, dragged_pos = None, piece = ''):
    
    WHITE = (245, 245, 220)
    BLACK = (120, 151, 76)
    window_size = 800
    square_size = window_size // 8
    image_size = window_size // 8 - 10
    image = pygame.image.load("pieces/pieces.png")
    # Main loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if not dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    square_x = mouse_x // square_size
                    square_y = mouse_y // square_size
                    with open("dragposes.txt", "w") as file:
                        file.write(str(square_x) + str(square_y))
                    file.close()
                    if 0 <= square_x < 8 and 0 <= square_y < 8:
                        piece = current_board[(square_x, square_y)]
                        if piece != '':
                            dragging = True
                            dragged_piece = piece
                            dragged_pos = (square_x, square_y)
                            
                            
                else:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    square_x2 = mouse_x // square_size
                    square_y2 = mouse_y // square_size
                    with open("dragposes.txt","r") as file:
                        data = file.read()
                        print(data)
                    file.close()
                    data = data.strip("\n")
                    mov = (int(data[0]), int(data[1]))
            
                    if (mov, (square_x2, square_y2)) in moves:
                            
                            if 0 <= square_x2 < 8 and 0 <= square_y2 < 8:
                                if (mov, (square_x2, square_y2)) == ((4,7),(6,7)):
                                    current_board[(7,7)] = ''
                                    current_board[(5,7)] = 'r'
                                if (mov, (square_x2, square_y2)) == ((4,7),(2,7)):
                                    current_board[(0,7)] = ''
                                    current_board[(3,7)] = 'r'
                                if (mov, (square_x2, square_y2)) == ((4,0),(6,0)):
                                    current_board[(7,0)] = ''
                                    current_board[(5,0)] = 'R'
                                if (mov, (square_x2, square_y2)) == ((4,0),(2,0)):
                                    current_board[(0,0)] = ''
                                    current_board[(3,0)] = 'R'
                                current_board[(square_x2, square_y2)] = piece
                                current_board[dragged_pos] = ''
                                dragging = False
                                dragged_piece = None
                                
                                break
                                
       
            else:
                if dragging:
                    dragging = False
                    dragged_piece = None
                    dragged_pos = (0,0)
                    piece = ""
                    with open("dragposes.txt","w") as file:
                        file.write("")
                    file.close()
                    

        # Draw the chessboard
    for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(window, color, (col * square_size, row * square_size, square_size, square_size))
        # Render the image onto specific squares (example: (0, 0) and (7, 7))
    blit_pieces(current_board, image, window, moves, dragging, dragged_piece)
    pygame.draw.rect(window, (211, 211, 211), (800, 0, 400, 800))
        # Update the display
    pygame.display.update()
    return [dragging, dragged_piece, dragged_pos, piece, ]
          # Bottom-right corner

    
    
    

