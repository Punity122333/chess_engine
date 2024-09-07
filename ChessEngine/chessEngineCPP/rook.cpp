#include "rook.h"
#include <map>
#include <vector>

// Rook move offsets
const std::pair<int, int> rook_offsets[4] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}
};

void check_rook(const std::map<std::pair<int, int>, char>& current_board, 
                std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;
        int chain = 1;
        
        // Check for white and black bishops
        if (piece_type == 'R' || piece_type == 'r') {
            for (const auto& offset : rook_offsets) {
                chain = 1;
                bool check = true;
                
                while (check) {
                    std::pair<int, int> target_position = {
                        position.first + chain * offset.first,
                        position.second + chain * offset.second
                    };
                    
                    // If target position is on the board
                    if (current_board.find(target_position) != current_board.end()) {
                        char target_piece = current_board.at(target_position);
                        if ((piece_type == 'R' && isupper(target_piece)) ||
                            (piece_type == 'r' && islower(target_piece))) {
                            check = false;
                            break;
                        }
                        // Determine if it's a valid move for black or white
                        if (piece_type == 'R' && (target_piece == ' ' || islower(target_piece))) {
                            moves_list['b'].push_back({position, target_position});
                        } else if (piece_type == 'r' && (target_piece == ' ' || isupper(target_piece))) {
                            moves_list['w'].push_back({position, target_position});
                        }
                        
                        // Stop if there's an enemy piece to capture
                        if ((piece_type == 'R' && islower(target_piece)) ||
                            (piece_type == 'r' && isupper(target_piece))) {
                            check = false;
                        }
                        
                    chain++;
                    } else {
                        check = false;
                    }
                }
            }
        }
    }
}
