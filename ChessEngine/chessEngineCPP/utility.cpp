#include "utility.h"
#include "king.h"

bool check_move(pair<int, int> start_pos, pair<int, int> end_pos, map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player) {
    for (const auto& move : moves_list[player]) {
        if (move.first == start_pos && move.second == end_pos) {
            return true;
        }
    }
    return false;
}

pair<vector<int>, vector<int>> update_kings_and_rooks_moved(pair<int, int> start_pos, pair<int, int> end_pos, vector<int>& has_kings_moved, vector<int>& has_rooks_moved, string player) {
    if (player == "b" && has_rooks_moved[0] == 0 && end_pos == make_pair(0, 7)) {
        has_rooks_moved[0] = -1;
    }
    if (start_pos == make_pair(0, 7) && has_rooks_moved[0] == 0) {
        has_rooks_moved[0] = 1;
    }
    if (player == "b" && has_rooks_moved[1] == 0 && end_pos == make_pair(7, 7)) {
        has_rooks_moved[1] = -1;
    }
    if (start_pos == make_pair(7, 7) && has_rooks_moved[1] == 0) {
        has_rooks_moved[1] = 1;
    }
    if (player == "w" && has_rooks_moved[2] == 0 && end_pos == make_pair(0, 0)) {
        has_rooks_moved[2] = -1;
    }
    if (start_pos == make_pair(0, 0) && has_rooks_moved[2] == 0) {
        has_rooks_moved[2] = 1;
    }
    if (player == "w" && has_rooks_moved[3] == 0 && end_pos == make_pair(7, 0)) {
        has_rooks_moved[3] = -1;
    }
    if (start_pos == make_pair(7, 0) && has_rooks_moved[3] == 0) {
        has_rooks_moved[3] = 1;
    }
    if (start_pos == make_pair(4, 0)) {
        has_kings_moved[1] = 1;
    }
    if (start_pos == make_pair(4, 7)) {
        has_kings_moved[0] = 1;
    }

    return make_pair(has_kings_moved, has_rooks_moved);
}

bool is_in_check(map<pair<int, int>, char>& current_board, map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player) {
    string opponent = (player == "b") ? "w" : "b";
    pair<int, int> king_pos = find_specific_king_pos(current_board, player[0]);

    for (const auto& mov : moves_list[opponent]) {
        if (mov.second == king_pos) {
            return true;
        }
    }
    return false;
}


bool is_attacking(map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player, pair<int, int> square) {
    for (const auto& mov : moves_list[player]) {
        if (mov.second == square) {
            return true;
        }
    }
    return false;
}
