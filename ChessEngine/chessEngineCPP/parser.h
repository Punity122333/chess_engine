#ifndef PARSE_MOVE_H
#define PARSE_MOVE_H

#include <map>
#include <string>
#include <utility>

using namespace std;

// Function to parse a chess move string and return the start and end positions as pairs
pair<pair<int, int>, pair<int, int>> parse_move(const string& move);

#endif // PARSE_MOVE_H
