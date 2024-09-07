#include <iostream>
#include <string>

using namespace std;
int main() {
    string board_state;

    // Read the board state from the standard input stream
    getline(std::cin, board_state);
    cout << board_state << endl;
    // Process the board state
    // ...

    return 0;
}