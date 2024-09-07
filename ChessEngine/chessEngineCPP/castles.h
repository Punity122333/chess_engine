#ifndef CASTLES_H
#define CASTLES_H

#include <vector>
#include <map>
#include <utility>
#include <string>

using namespace std;

// Function declaration for check_castling
pair<vector<pair<pair<int, int>, pair<int, int>>>, map<char, vector<pair<pair<int, int>, pair<int, int>>>>> 
check_castling(map<pair<int, int>, char>& current_board, 
               map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
               vector<int>& has_kings_moved, 
               vector<int>& has_rooks_moved, 
               const char& player);

// Declaration for helper functions (presumed, if used in your function)
bool is_in_check(const map<pair<int, int>, char>& board, 
                 const map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
                 const char& player);

bool is_attacking(const map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
                  const char& opponent, 
                  const pair<int, int>& position);

#endif // CASTLES_H
