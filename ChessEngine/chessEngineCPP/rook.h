#ifndef ROOK_H
#define ROOK_H

#include <map>
#include <vector>
#include <utility> // for std::pair

// Function to check valid rook moves for both players
void check_rook(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

#endif // ROOK_H
