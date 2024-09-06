#include "knight.h"
#include <map>
#include <vector>

// Knight move offsets
const std::pair<int, int> knight_offsets[8] = {
    {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
    {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
};

void check_knight(const std::map<std::pair<int, int>, char>& current_board, 
                  std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;
        
        if (piece_type == 'N') {
            // White knight moves
            for (const auto& offset : knight_offsets) {
                std::pair<int, int> new_pos = {position.first + offset.first, position.second + offset.second};
                if (current_board.find(new_pos) != current_board.end() && 
                    (islower(current_board.at(new_pos)) || current_board.at(new_pos) == ' ')) 
                {
                    moves_list['b'].emplace_back(position, new_pos);
                }
            }
        } 
        else if (piece_type == 'n') {
            // Black knight moves
            for (const auto& offset : knight_offsets) {
                std::pair<int, int> new_pos = {position.first + offset.first, position.second + offset.second};
                if (current_board.find(new_pos) != current_board.end() && 
                    (isupper(current_board.at(new_pos)) || current_board.at(new_pos) == ' ')) 
                {
                    moves_list['w'].emplace_back(position, new_pos);
                }
            }
        }
    }
}
