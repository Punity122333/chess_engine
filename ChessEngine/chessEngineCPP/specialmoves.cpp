#include "specialmoves.h"
#include "utility.h"
#include <vector>
#include <map>
#include <utility>
#include <string>
#include <iostream>

using namespace std;

pair<vector<pair<pair<int, int>, pair<int, int>>>, map<char, vector<pair<pair<int, int>, pair<int, int>>>>>  
check_en_passant(const map<pair<int, int>, char>& current_board, 
                 const map<pair<int, int>, char>& prev_board, 
                 map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
                 const char& player) {
    
    vector<pair<pair<int, int>, pair<int, int>>> can_passant;

    if (player == 'b') {
        for (const auto& [k, v] : current_board) {
            if (v == 'P' && k.second == 3) {
                if (prev_board.at({k.first, k.second - 2}) == 'P') {
                    if (current_board.count({k.first - 1, k.second}) && current_board.at({k.first - 1, k.second}) == 'p') {
                        moves_list[player].emplace_back(make_pair(make_pair(k.first - 1, k.second), make_pair(k.first, k.second - 1)));
                        can_passant.emplace_back(make_pair(make_pair(k.first - 1, k.second), make_pair(k.first, k.second - 1)));
                    }
                    if (current_board.count({k.first + 1, k.second}) && current_board.at({k.first + 1, k.second}) == 'p') {
                        moves_list[player].emplace_back(make_pair(make_pair(k.first + 1, k.second), make_pair(k.first, k.second - 1)));
                        can_passant.emplace_back(make_pair(make_pair(k.first + 1, k.second), make_pair(k.first, k.second - 1)));
                    }
                }
            }
        }
    } else if (player == 'w') {
        for (const auto& [k, v] : current_board) {
            if (v == 'p' && k.second == 4) {
                if (prev_board.at({k.first, k.second + 2}) == 'p') {
                    if (current_board.count({k.first - 1, k.second}) && current_board.at({k.first - 1, k.second}) == 'P') {
                        moves_list[player].emplace_back(make_pair(make_pair(k.first - 1, k.second), make_pair(k.first, k.second + 1)));
                        can_passant.emplace_back(make_pair(make_pair(k.first - 1, k.second), make_pair(k.first, k.second + 1)));
                    }
                    if (current_board.count({k.first + 1, k.second}) && current_board.at({k.first + 1, k.second}) == 'P') {
                        moves_list[player].emplace_back(make_pair(make_pair(k.first + 1, k.second), make_pair(k.first, k.second + 1)));
                        can_passant.emplace_back(make_pair(make_pair(k.first + 1, k.second), make_pair(k.first, k.second + 1)));
                    }
                }
            }
        }
    }
    
    return {can_passant, moves_list};
}


