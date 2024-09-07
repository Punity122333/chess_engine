#include "king.h"
#include <map>
#include <vector>

// King move offsets
const std::pair<int, int> king_offsets[8] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1},
    {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
};

void check_king(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;

        if (piece_type == 'k') { // White king
            for (const auto& offset : king_offsets) {
                std::pair<int, int> new_pos = {position.first + offset.first, position.second + offset.second};
                if (current_board.find(new_pos) != current_board.end() &&
                    (isupper(current_board.at(new_pos)) || current_board.at(new_pos) == ' ')) 
                {
                    moves_list['w'].emplace_back(position, new_pos);
                }
            }
        } 
        else if (piece_type == 'K') { // Black king
            for (const auto& offset : king_offsets) {
                std::pair<int, int> new_pos = {position.first + offset.first, position.second + offset.second};
                if (current_board.find(new_pos) != current_board.end() &&
                    (islower(current_board.at(new_pos)) || current_board.at(new_pos) == ' ')) 
                {
                    moves_list['b'].emplace_back(position, new_pos);
                }
            }
        }
    }
}

std::vector<std::pair<int, int>> find_king_pos(const std::map<std::pair<int, int>, char>& current_board, 
                                               char player) 
{
    std::vector<std::pair<int, int>> positions;

    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;

        if ((player == 'w' && piece_type == 'k') || (player == 'b' && piece_type == 'K')) {
            positions.push_back(position);
            for (const auto& offset : king_offsets) {
                std::pair<int, int> new_pos = {position.first + offset.first, position.second + offset.second};
                if (current_board.find(new_pos) != current_board.end() &&
                    ((player == 'w' && !islower(current_board.at(new_pos))) ||
                     (player == 'b' && !isupper(current_board.at(new_pos))))) 
                {
                    positions.push_back(new_pos);
                }
            }
        }
    }

    return positions;
}

std::pair<int, int> find_specific_king_pos(const std::map<std::pair<int, int>, char>& current_board, 
                                           char player) 
{
    for (const auto& piece : current_board) {
        if ((player == 'b' && piece.second == 'K') ||
            (player == 'w' && piece.second == 'k')) 
        {
            return piece.first;
        }
    }

    // Return an invalid position if no king is found
    return {-1, -1}; // Invalid position
}
