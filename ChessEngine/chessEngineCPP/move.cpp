#include "move.h"
#include <iostream>
#include <map>
#include <vector>
#include <algorithm> // For std::find

void make_move(const std::pair<int, int>& start_pos, const std::pair<int, int>& end_pos,
               std::map<std::pair<int, int>, char>& current_board,
               const std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& can_passant,
               const std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& castles,
               const std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list,
               char player, bool check_promotion) 
{
    // The pair you're searching for should be std::pair<std::pair<int, int>, std::pair<int, int>>
    std::pair<std::pair<int, int>, std::pair<int, int>> move_to_check = std::make_pair(start_pos, end_pos);

    // Check if the move is in the player's valid moves list
    auto valid_move = std::find(moves_list.at(player).begin(), moves_list.at(player).end(), move_to_check);
    if (valid_move != moves_list.at(player).end()) 
    {
        // Handle Castling
        auto castle_move = std::find(castles.begin(), castles.end(), move_to_check);
        if (castle_move != castles.end()) {
            if (start_pos == std::make_pair(4, 7) && end_pos == std::make_pair(6, 7)) {
                current_board[{5, 7}] = 'r'; // Move rook for black kingside castling
                current_board[{7, 7}] = ' ';
            } 
            else if (start_pos == std::make_pair(4, 0) && end_pos == std::make_pair(6, 0)) {
                current_board[{5, 0}] = 'R'; // Move rook for white kingside castling
                current_board[{7, 0}] = ' ';
            } 
            else if (start_pos == std::make_pair(4, 7) && end_pos == std::make_pair(2, 7)) {
                current_board[{3, 7}] = 'r'; // Move rook for black queenside castling
                current_board[{0, 7}] = ' ';
            } 
            else if (start_pos == std::make_pair(4, 0) && end_pos == std::make_pair(2, 0)) {
                current_board[{3, 0}] = 'R'; // Move rook for white queenside castling
                current_board[{0, 0}] = ' ';
            }
        }

        // Handle Promotion
        char piece = current_board[start_pos];
        if (check_promotion) {
            if (piece == 'p' && player == 'w' && end_pos.second == 0) {
                piece = 'q'; // Promote white pawn to queen
            } else if (piece == 'P' && player == 'b' && end_pos.second == 7) {
                piece = 'Q'; // Promote black pawn to queen
            }
        }

        // Make the move on the board
        current_board[end_pos] = piece;
        current_board[start_pos] = ' ';

        // Handle En Passant
        auto en_passant_move = std::find(can_passant.begin(), can_passant.end(), move_to_check);
        if (en_passant_move != can_passant.end()) {
            if (player == 'w') {
                current_board[{end_pos.first, end_pos.second + 1}] = ' '; // Capture en passant for white
            } else if (player == 'b') {
                current_board[{end_pos.first, end_pos.second - 1}] = ' '; // Capture en passant for black
            }
        }

    } else {
        std::cout << start_pos.first << "," << start_pos.second << " to " << end_pos.first << "," 
                  << end_pos.second << " is not a valid move!" << std::endl;
        std::cout << "Move not possible!" << std::endl;
    }
}
