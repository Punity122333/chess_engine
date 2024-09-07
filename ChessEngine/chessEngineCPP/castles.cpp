#include "utility.h"
#include "castles.h"
#include <vector>
#include <map>
#include <utility>
#include <string>
#include <iostream>

using namespace std;

pair<vector<pair<pair<int, int>, pair<int, int>>>, map<char, vector<pair<pair<int, int>, pair<int, int>>>>> 
check_castling(map<pair<int, int>, char>& current_board, 
               map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
               vector<int>& has_kings_moved, 
               vector<int>& has_rooks_moved, 
               const char& player) {
    
    vector<pair<pair<int, int>, pair<int, int>>> castles;
    
    char opponent = (player == 'w') ? 'b' : 'w';
    
    if (player == 'w' && current_board.at({7, 7}) == 'r') {
        
        if (current_board.at({5, 7}) == ' ' && current_board.at({6, 7}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {5, 7}) && !is_attacking(moves_list, opponent, {6, 7})) {
            moves_list[player].emplace_back(make_pair(make_pair(4, 7), make_pair(6, 7)));
            castles.emplace_back(make_pair(make_pair(4, 7), make_pair(6, 7)));
        }
    }

    

    if (player == 'b' && current_board.at({7,0}) == 'R') {
        if (current_board.at({5, 0}) == ' ' && current_board.at({6, 0}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {5, 0}) && !is_attacking(moves_list, opponent, {6, 0})) {
            moves_list[player].emplace_back(make_pair(make_pair(4, 0), make_pair(6, 0)));
            castles.emplace_back(make_pair(make_pair(4, 0), make_pair(6, 0)));
        }
    }

    // Left-side castling for white
    if (player == 'w' && current_board.at({0,7}) == 'r') {
        if (current_board.at({1, 7}) == ' ' && current_board.at({2, 7}) == ' ' && current_board.at({3, 7}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {1, 7}) && !is_attacking(moves_list, opponent, {2, 7}) && !is_attacking(moves_list, opponent, {3, 7})) {
            moves_list[player].emplace_back(make_pair(make_pair(4, 7), make_pair(2, 7)));
            castles.emplace_back(make_pair(make_pair(4, 7), make_pair(2, 7)));
        }
    }

    // Left-side castling for black
    if (player == 'w' && current_board.at({0, 0}) == 'R') {
        if (current_board.at({1, 0}) == ' ' && current_board.at({2, 0}) == ' ' && current_board.at({3, 0}) == ' ' &&
            !is_in_check(current_board, moves_list, player) && 
            !is_attacking(moves_list, opponent, {1, 0}) && !is_attacking(moves_list, opponent, {2, 0}) && !is_attacking(moves_list, opponent, {3, 0})) {
            moves_list[player].emplace_back(make_pair(make_pair(4, 0), make_pair(2, 0)));
            castles.emplace_back(make_pair(make_pair(4, 0), make_pair(2, 0)));
        }
    }
    
    return {castles, moves_list};
}