#include <map>
#include <vector>
#include <utility>
#include <ctype.h>
#include <iostream>


using namespace std;

pair<pair<int, int>, pair<int, int>> parse_move(const string& move) {
    map<char, int> alphdict = {{'a',1},{'b',2},{'c',3},{'d',4},{'e',5},{'f',6},{'g',7},{'h',8}};
    pair<int, int> start, end;
    string startpos = move.substr(0,2);
    string endpos = move.substr(2,2);
    start.first = alphdict[startpos[0]] - 1;
    start.second = 8 - (startpos[1] - '0');
    end.first = alphdict[endpos[0]] - 1;
    end.second = 8 -(endpos[1] - '0');
    return make_pair(start, end);

}