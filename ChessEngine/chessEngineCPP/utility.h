#ifndef UTILITY_H
#define UTILITY_H

#include <utility>
#include <vector>
#include <string>
#include <map>

using namespace std;

bool check_move(pair<int, int> start_pos, pair<int, int> end_pos, map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player = "w");
pair<vector<int>, vector<int>> update_kings_and_rooks_moved(pair<int, int> start_pos, pair<int, int> end_pos, vector<int>& has_kings_moved, vector<int>& has_rooks_moved, string player = "w");
bool is_in_check(map<pair<int, int>, char>& current_board, map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player);
bool is_attacking(map<string, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, string player, pair<int, int> square);

#endif
