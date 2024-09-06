#include "queen.h"
#include <map>
#include <vector>

// Queen move offsets (rook + bishop)
const std::pair<int, int> queen_offsets[8] = {
    {1, 0}, {-1, 0}, {0, 1}, {0, -1}, // Rook-like moves
    {1, 1}, {1, -1}, {-1, 1}, {-1, -1} // Bishop-like moves
};

void check_queen(const std::map<std::pair<int, int>, char>& current_board, 
                  std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;
        int chain = 1;
        
        // Check for white and black bishops
        if (piece_type == 'Q' || piece_type == 'q') {
            for (const auto& offset : queen_offsets) {
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
                        if ((piece_type == 'Q' && isupper(target_piece)) ||
                            (piece_type == 'q' && islower(target_piece))) {
                            check = false;
                            break;
                        }
                        // Determine if it's a valid move for black or white
                        if (piece_type == 'Q' && (target_piece == ' ' || islower(target_piece))) {
                            moves_list['b'].push_back({position, target_position});
                        } else if (piece_type == 'q' && (target_piece == ' ' || isupper(target_piece))) {
                            moves_list['w'].push_back({position, target_position});
                        }
                        
                        // Stop if there's an enemy piece to capture
                        if ((piece_type == 'Q' && islower(target_piece)) ||
                            (piece_type == 'q' && isupper(target_piece))) {
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
