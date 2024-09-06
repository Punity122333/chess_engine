#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>
#include "pawn.h"
#include "knight.h"
#include "rook.h"
#include "bishop.h"
#include "queen.h"
#include "king.h"
#include "move.h"

using namespace std;

// Function to remove illegal moves from the move list
map<char, vector<pair<pair<int, int>, pair<int, int>>>> remove_illegal_moves(
    map<pair<int, int>, char>& current_board, 
    map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
    vector<pair<pair<int, int>, pair<int, int>>>& can_passant, 
    vector<pair<pair<int, int>, pair<int, int>>>& castles, 
    char player) 
{
    // Copying current board and move list
    map<pair<int, int>, char> current_board2 = current_board;
    map<char, vector<pair<pair<int, int>, pair<int, int>>>> moves_list_copy = moves_list;
    map<char, vector<pair<pair<int, int>, pair<int, int>>>> moves_list2 = { {'w', {}}, {'b', {}} };

    // Find the king position of the current player
    pair<int, int> king_pos = find_king_pos(current_board2, player).front();
    char opponent = (player == 'b') ? 'w' : 'b';
    vector<pair<pair<int, int>, pair<int, int>>> deleted_moves;

    // Iterating through the move list for the current player
    for (const auto& mov : moves_list_copy[player]) {
        // Skip castling moves
        if (find(castles.begin(), castles.end(), mov) != castles.end()) continue;

        // Copy the board state again and reset moves_list2
        current_board2 = current_board;
        moves_list2 = { {'w', {}}, {'b', {}} };

        // Make the move and check the board state for the opponent's potential responses
        make_move(mov.first, mov.second, current_board2, can_passant, castles, moves_list, player, false);

        check_bishop(current_board2, moves_list2);
        check_knight(current_board2, moves_list2);
        check_king(current_board2, moves_list2);
        check_queen(current_board2, moves_list2);
        check_rook(current_board2, moves_list2);
        check_pawn(current_board2, moves_list2);

        // Check if the opponent can attack the king after this move
        for (const auto& mov2 : moves_list2[opponent]) {
            if (mov2.second == find_specific_king_pos(current_board2, player)) {
                deleted_moves.push_back(mov);
            }
        }
    }

    // Remove moves that capture opponent's piece incorrectly
    for (const auto& mov : moves_list[player]) {
        if (player == 'w' && current_board.count(mov.second) && islower(current_board[mov.second])) {
            deleted_moves.push_back(mov);
        }
        if (player == 'b' && current_board.count(mov.second) && isupper(current_board[mov.second])) {
            deleted_moves.push_back(mov);
        }
    }

    // Remove deleted moves from the original move list
    for (const auto& mov : deleted_moves) {
        moves_list_copy[player].erase(remove(moves_list_copy[player].begin(), moves_list_copy[player].end(), mov), moves_list_copy[player].end());
    }

    // Rechecking all moves after removal to ensure consistency
    map<char, vector<pair<pair<int, int>, pair<int, int>>>> moves_list_copy2 = { {'w', {}}, {'b', {}} };
    check_bishop(current_board, moves_list_copy2);
    check_knight(current_board, moves_list_copy2);
    check_pawn(current_board, moves_list_copy2);
    check_rook(current_board, moves_list_copy2);
    check_queen(current_board, moves_list_copy2);
    check_king(current_board, moves_list_copy2);

    for (auto it = moves_list_copy[player].begin(); it != moves_list_copy[player].end(); ) {
        if (find(moves_list_copy2[player].begin(), moves_list_copy2[player].end(), *it) == moves_list_copy2[player].end() &&
            it->first != king_pos && it->second != king_pos) {
            it = moves_list_copy[player].erase(it);
        } else {
            ++it;
        }
    }

    // Remove invalid king moves (if any)
    for (auto it = moves_list_copy[player].begin(); it != moves_list_copy[player].end(); ) {
        if (tolower(current_board[it->first]) == 'k' && 
            abs(it->first.first - it->second.first) + abs(it->first.second - it->second.second) > 2) {
            it = moves_list_copy[player].erase(it);
        } else {
            ++it;
        }
    }

    return moves_list_copy;
}
