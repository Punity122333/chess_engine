#ifndef REMOVE_ILLEGAL_MOVES_H
#define REMOVE_ILLEGAL_MOVES_H

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>

// Function declarations for all the external dependencies
std::vector<std::pair<int, int>> find_king_pos(const std::map<std::pair<int, int>, char>& board, char player);
std::pair<int, int> find_specific_king_pos(const std::map<std::pair<int, int>, char>& board, char player);
void make_move(std::pair<int, int> from, std::pair<int, int> to, std::map<std::pair<int, int>, char>& board,
               std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& can_passant, 
               std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& castles,
               std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list,
               char player, bool is_simulation);
void check_bishop(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);
void check_knight(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);
void check_rook(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);
void check_pawn(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);
void check_queen(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);
void check_king(const std::map<std::pair<int, int>, char>& board, std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

// Function declaration for remove_illegal_moves
std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>> remove_illegal_moves(
    std::map<std::pair<int, int>, char>& current_board, 
    std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list, 
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& can_passant, 
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& castles, 
    char player
);

#endif // REMOVE_ILLEGAL_MOVES_H
