#include "pawn.h"
#include <map>
#include <vector>
#include <utility>
#include <string.h>

void check_pawn(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;
        
        if (piece_type == 'P') {
            // White pawn moves
            if (position.second == 1 && current_board.find({position.first, position.second + 1}) != current_board.end() &&
            current_board.at({position.first, position.second + 1}) == ' ') {
                
                if (position.second == 1 && current_board.at({position.first, position.second + 2}) == ' ') {
                    moves_list['b'].emplace_back(position, std::make_pair(position.first, position.second + 2));
                }
            }
            if (current_board.at({position.first, position.second + 1}) == ' ') {
                moves_list['b'].emplace_back(position, std::make_pair(position.first, position.second + 1));
            }
            if (position.first > 0 && current_board.find({position.first - 1, position.second + 1}) != current_board.end() &&
                strchr("pnbrqk", current_board.at({position.first - 1, position.second + 1}))) 
            {
                moves_list['b'].emplace_back(position, std::make_pair(position.first - 1, position.second + 1));
            }
            if (position.first < 7 && current_board.find({position.first + 1, position.second + 1}) != current_board.end() &&
                strchr("pnbrqk", current_board.at({position.first + 1, position.second + 1}))) 
            {
                moves_list['b'].emplace_back(position, std::make_pair(position.first + 1, position.second + 1));
            }
        }
        else if (piece_type == 'p') {
            // Black pawn moves
            if (position.second == 6 && current_board.find({position.first, position.second - 1}) != current_board.end() &&
            current_board.at({position.first, position.second - 1}) == ' ') {
                
                if (position.second == 6 && current_board.at({position.first, position.second - 2}) == ' ') {
                    moves_list['w'].emplace_back(position, std::make_pair(position.first, position.second - 2));
                }
            }
            if (current_board.at({position.first, position.second - 1}) == ' ') {
                moves_list['w'].emplace_back(position, std::make_pair(position.first, position.second - 1));
            }
            if (position.first > 0 && current_board.find({position.first - 1, position.second - 1}) != current_board.end() &&
                strchr("PNBRQK", current_board.at({position.first - 1, position.second - 1}))) 
            {
                moves_list['w'].emplace_back(position, std::make_pair(position.first - 1, position.second - 1));
            }
            if (position.first < 7 && current_board.find({position.first + 1, position.second - 1}) != current_board.end() &&
                strchr("PNBRQK", current_board.at({position.first + 1, position.second - 1}))) 
            {
                moves_list['w'].emplace_back(position, std::make_pair(position.first + 1, position.second - 1));
            }
        }
    }
}
