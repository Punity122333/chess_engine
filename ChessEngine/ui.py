import pygame
import sys

white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = {(0, 0):'R', (1, 0):'N', (2, 0):'B', (3, 0):'Q', (4, 0):'K', (5, 0):'B', (6, 0):'N', (7, 0):'R',
                   (0, 1):'P', (1, 1):'P', (2, 1):'P', (3, 1):'P', (4, 1):'P', (5, 1):'P', (6, 1):'P', (7, 1):'P'}
white_locations = {(0, 7):'r', (1, 7):'n', (2, 7):'b', (3, 7):'q', (4, 7):'k', (5, 7):'b', (6, 7):'n', (7, 7):'r',
                   (0, 6):'p', (1, 6):'p', (2, 6):'p', (3, 6):'p', (4, 6):'p', (5, 6):'p', (6, 6):'p', (7, 6):'p'}
black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

        

def blit_pieces(current_board: dict, image: pygame.image, window: pygame.display):
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
        
        
        


def gen_ui(current_board: dict, moves_list: dict, window):
    
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

        # Draw the chessboard
    for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(window, color, (col * square_size, row * square_size, square_size, square_size))
        # Render the image onto specific squares (example: (0, 0) and (7, 7))
    blit_pieces(current_board, image, window)
        # Update the display
    pygame.display.update()
        
          # Bottom-right corner
    


    
    


