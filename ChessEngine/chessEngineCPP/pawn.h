#ifndef PAWN_H
#define PAWN_H

#include <map>
#include <vector>
#include <utility> // for std::pair

// Function to check valid pawn moves for both players
void check_pawn(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

#endif // PAWN_H
