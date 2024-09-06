#include "specialmoves.h"
#include "utility.h"
#include <vector>
#include <map>
#include <utility>
#include <string>

std::pair<std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>, std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>> 
check_en_passant(const std::map<std::pair<int, int>, char>& current_board, 
                 const std::map<std::pair<int, int>, char>& prev_board, 
                 std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list, 
                 const std::string& player) {
    
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> can_passant;

    if (player == "b") {
        for (const auto& [k, v] : current_board) {
            if (v == 'P' && k.second == 3) {
                if (prev_board.at({k.first, k.second - 2}) == 'P') {
                    if (current_board.count({k.first - 1, k.second}) && current_board.at({k.first - 1, k.second}) == 'p') {
                        moves_list[player].emplace_back(std::make_pair(std::make_pair(k.first - 1, k.second), std::make_pair(k.first, k.second - 1)));
                        can_passant.emplace_back(std::make_pair(std::make_pair(k.first - 1, k.second), std::make_pair(k.first, k.second - 1)));
                    }
                    if (current_board.count({k.first + 1, k.second}) && current_board.at({k.first + 1, k.second}) == 'p') {
                        moves_list[player].emplace_back(std::make_pair(std::make_pair(k.first + 1, k.second), std::make_pair(k.first, k.second - 1)));
                        can_passant.emplace_back(std::make_pair(std::make_pair(k.first + 1, k.second), std::make_pair(k.first, k.second - 1)));
                    }
                }
            }
        }
    } else if (player == "w") {
        for (const auto& [k, v] : current_board) {
            if (v == 'p' && k.second == 4) {
                if (prev_board.at({k.first, k.second + 2}) == 'p') {
                    if (current_board.count({k.first - 1, k.second}) && current_board.at({k.first - 1, k.second}) == 'P') {
                        moves_list[player].emplace_back(std::make_pair(std::make_pair(k.first - 1, k.second), std::make_pair(k.first, k.second + 1)));
                        can_passant.emplace_back(std::make_pair(std::make_pair(k.first - 1, k.second), std::make_pair(k.first, k.second + 1)));
                    }
                    if (current_board.count({k.first + 1, k.second}) && current_board.at({k.first + 1, k.second}) == 'P') {
                        moves_list[player].emplace_back(std::make_pair(std::make_pair(k.first + 1, k.second), std::make_pair(k.first, k.second + 1)));
                        can_passant.emplace_back(std::make_pair(std::make_pair(k.first + 1, k.second), std::make_pair(k.first, k.second + 1)));
                    }
                }
            }
        }
    }

    return {can_passant, moves_list};
}

std::pair<std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>, std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>> 
check_castling(std::map<std::pair<int, int>, char>& current_board, 
               std::map<std::string, std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>>>& moves_list, 
               std::vector<int>& has_kings_moved, 
               std::vector<int>& has_rooks_moved, 
               const std::string& player) {
    
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> castles;
    std::string opponent = (player == "w") ? "b" : "w";

    if (player == "w" && current_board.at({7, 7}) == 'r' && has_kings_moved[0] == 0 && has_rooks_moved[1] == 0) {
        if (current_board.at({5, 7}) == ' ' && current_board.at({6, 7}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {5, 7}) && !is_attacking(moves_list, opponent, {6, 7})) {
            moves_list[player].emplace_back(std::make_pair(std::make_pair(4, 7), std::make_pair(6, 7)));
            castles.emplace_back(std::make_pair(std::make_pair(4, 7), std::make_pair(6, 7)));
        }
    }

    if (player == "b" && current_board.at({7,0}) == 'R' && has_kings_moved[1] == 0 && has_rooks_moved[3] == 0) {
        if (current_board.at({5, 0}) == ' ' && current_board.at({6, 0}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {5, 0}) && !is_attacking(moves_list, opponent, {6, 0})) {
            moves_list[player].emplace_back(std::make_pair(std::make_pair(4, 0), std::make_pair(6, 0)));
            castles.emplace_back(std::make_pair(std::make_pair(4, 0), std::make_pair(6, 0)));
        }
    }

    // Left-side castling for white
    if (player == "w" && current_board.at({0,7}) == 'r' && has_kings_moved[0] == 0 && has_rooks_moved[0] == 0) {
        if (current_board.at({1, 7}) == ' ' && current_board.at({2, 7}) == ' ' && current_board.at({3, 7}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {1, 7}) && !is_attacking(moves_list, opponent, {2, 7}) && !is_attacking(moves_list, opponent, {3, 7})) {
            moves_list[player].emplace_back(std::make_pair(std::make_pair(4, 7), std::make_pair(2, 7)));
            castles.emplace_back(std::make_pair(std::make_pair(4, 7), std::make_pair(2, 7)));
        }
    }

    // Left-side castling for black
    if (player == "b" && current_board.at({0, 0}) == 'R' && has_kings_moved[1] == 0 && has_rooks_moved[2] == 0) {
        if (current_board.at({1, 0}) == ' ' && current_board.at({2, 0}) == ' ' && current_board.at({3, 0}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {1, 0}) && !is_attacking(moves_list, opponent, {2, 0}) && !is_attacking(moves_list, opponent, {3, 0})) {
            moves_list[player].emplace_back(std::make_pair(std::make_pair(4, 0), std::make_pair(2, 0)));
            castles.emplace_back(std::make_pair(std::make_pair(4, 0), std::make_pair(2, 0)));
        }
    }

    return {castles, moves_list};
}
