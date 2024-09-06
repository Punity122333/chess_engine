#ifndef CHESS_H
#define CHESS_H

#include <map>
#include <vector>
#include <string>
#include "bishop.h"
#include "king.h"
#include "knight.h"
#include "move.h"
#include "pawn.h"
#include "queen.h"
#include "rook.h"

// Global variables
extern std::map<std::pair<int, int>, char> board;  // The chessboard
extern char current_player;  // 'w' for white, 'b' for black
extern std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> move_history;  // Move history
extern std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> castles;  // Available castling moves
extern std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> en_passant_moves;  // Available en passant moves

// Function declarations
void initialize_board();  // Set up the initial board
void play();  // Main game loop
bool is_game_over();  // Check if the game is over
void display_board();  // Display the current state of the board
void make_move(const std::pair<int, int>& start_pos, const std::pair<int, int>& end_pos);  // Handles move logic
void check_castling();  // Special case handling for castling
void check_promotion();  // Special case handling for promotion

void check_en_passant();  // Special case handling for en passant
bool is_valid_move(const std::pair<int, int>& start_pos, const std::pair<int, int>& end_pos);  // Check if move is valid

#endif // CHESS_H
