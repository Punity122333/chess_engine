#ifndef KING_H
#define KING_H

#include <map>
#include <vector>
#include <utility> // for std::pair

// Function to check valid king moves for both players
void check_king(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

// Function to find possible king positions for a player
std::vector<std::pair<int, int>> find_king_pos(const std::map<std::pair<int, int>, char>& current_board, 
                                               char player);

// Function to find specific king position for a player
std::pair<int, int> find_specific_king_pos(const std::map<std::pair<int, int>, char>& current_board, 
                                           char player);

#endif // KING_H
