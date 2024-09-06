#ifndef QUEEN_H
#define QUEEN_H

#include <map>
#include <vector>
#include <utility> // for std::pair

// Function to check valid queen moves for both players
void check_queen(const std::map<std::pair<int, int>, char>& current_board, 
                  std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list);

#endif // QUEEN_H
