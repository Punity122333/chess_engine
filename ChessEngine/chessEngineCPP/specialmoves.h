#ifndef SPECIALMOVES_H
#define SPECIALMOVES_H

#include <map>
#include <vector>
#include <utility>
#include <string>

// Function declarations
std::pair<std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>, std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>> 
check_en_passant(const std::map<std::pair<int, int>, char>& current_board, 
                 const std::map<std::pair<int, int>, char>& prev_board, 
                 std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list, 
                 const std::string& player);

std::pair<std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>, std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>> 
check_castling(const std::map<std::pair<int, int>, char>& current_board, 
               std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list, 
               const std::vector<int>& has_kings_moved, 
               const std::vector<int>& has_rooks_moved, 
               const std::string& player);

#endif // SPECIALMOVES_H
