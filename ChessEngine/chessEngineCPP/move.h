#ifndef MOVE_H
#define MOVE_H

#include <map>
#include <vector>
#include <utility> // for std::pair
#include <string>

// Function to make a move on the chess board
void make_move(const std::pair<int, int>& start_pos, const std::pair<int, int>& end_pos,
               std::map<std::pair<int, int>, char>& current_board,
               const std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& can_passant,
               const std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>& castles,
               const std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list,
               char player = 'w', bool check_promotion = true);

#endif // MOVE_H
