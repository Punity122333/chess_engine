#ifndef SPECIALMOVES_H
#define SPECIALMOVES_H

#include <map>
#include <vector>
#include <utility>
#include <string>

using namespace std;

// Function declarations
pair<vector<pair<pair<int, int>, pair<int, int>>>, map<char, vector<pair<pair<int, int>, pair<int, int>>>>> 
check_en_passant(const map<pair<int, int>, char>& current_board, 
                 const map<pair<int, int>, char>& prev_board, 
                 map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
                 const char& player);

pair<vector<pair<pair<int, int>, pair<int, int>>>, map<char, vector<pair<pair<int, int>, pair<int, int>>>>> 
check_castling(const map<pair<int, int>, char>& current_board, 
               map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list, 
               const vector<int>& has_kings_moved, 
               const vector<int>& has_rooks_moved, 
               const char& player);

#endif // SPECIALMOVES_H
