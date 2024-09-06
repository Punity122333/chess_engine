#include "bishop.h"
#include <map>
#include <vector>
#include <utility>
#include <ctype.h>
#include <iostream>

const std::vector<std::pair<int, int>> bishop_offsets = {
    {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
};

void check_bishop(const std::map<std::pair<int, int>, char>& current_board, 
                  std::map<char, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list) 
{
    for (const auto& piece : current_board) {
        std::pair<int, int> position = piece.first;
        char piece_type = piece.second;
        int chain = 1;
        
        // Check for white and black bishops
        if (piece_type == 'B' || piece_type == 'b') {
            for (const auto& offset : bishop_offsets) {
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
                        if ((piece_type == 'B' && isupper(target_piece)) ||
                            (piece_type == 'b' && islower(target_piece))) {
                            check = false;
                            break;
                        }
                        // Determine if it's a valid move for black or white
                        if (piece_type == 'B' && (target_piece == ' ' || islower(target_piece))) {
                            moves_list['b'].push_back({position, target_position});
                        } else if (piece_type == 'b' && (target_piece == ' ' || isupper(target_piece))) {
                            moves_list['w'].push_back({position, target_position});
                        }
                        
                        // Stop if there's an enemy piece to capture
                        if ((piece_type == 'B' && islower(target_piece)) ||
                            (piece_type == 'b' && isupper(target_piece))) {
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
