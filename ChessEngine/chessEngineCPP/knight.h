#ifndef KNIGHT_H
#define KNIGHT_H

#include <map>
#include <vector>
#include <utility> // for std::pair

// Function to check valid knight moves for both players
void check_knight(const std::map<std::pair<int, int>, char>& current_board, 
                  std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

#endif // KNIGHT_H
