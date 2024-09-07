#include "chess.h"
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>
#include "pawn.h"
#include "knight.h"
#include "rook.h"
#include "bishop.h"
#include "queen.h"
#include "king.h"
#include "move.h"
#include "specialmoves.h"
#include "illegal_removal.h"
#include "parser.h"
#include "specialmoves.h"
#include "castles.h"
#include <iostream>
#include <algorithm>

using namespace std;

// Global variables initialization
map<pair<int, int>, char> board;


bool is_valid_move(const pair<int, int>& start_pos, const pair<int, int>& end_pos, map<char, vector<pair<pair<int, int>, pair<int, int>>>> moves_list) {
    pair<pair<int, int>, pair<int, int>> move= {start_pos, end_pos};
    // Count of moves in moves_list for each player is being checked
    if (count(moves_list['w'].begin(), moves_list['w'].end(), move) != 0 || count(moves_list['b'].begin(), moves_list['b'].end(), move) != 0 ) {
        return true;
    }
    else {
        return false;
    }
    
}


void initialize_board(map<pair<int, int>, char>& board) {
    // Clear the board
    board.clear();

    // Place white pieces (rows 6 and 7)
    for (int col = 0; col < 8; ++col) {
        // White pawns in row 6
        // Black pawns in row 1
        board[{col, 6}] = 'p';
        // Black pieces in row 0
        if (col == 0 || col == 7) board[{col, 7}] = 'r'; // Rooks
        if (col == 1 || col == 6) board[{col, 7}] = 'n'; // Knights
        if (col == 2 || col == 5) board[{col, 7}] = 'b'; // Bishops
        if (col == 3) board[{col, 7}] = 'q'; // Queen
        if (col == 4) board[{col, 7}] = 'k'; // King
    }

    // Place black pieces (rows 0 and 1)
    for (int col = 0; col < 8; ++col) {
        
        board[{col, 1}] = 'P';
        // White pieces in row 7
        if (col == 0 || col == 7) board[{col, 0}] = 'R'; // Rooks
        if (col == 1 || col == 6) board[{col, 0}] = 'N'; // Knights
        if (col == 2 || col == 5) board[{col, 0}] = 'B'; // Bishops
        if (col == 3) board[{col, 0}] = 'Q'; // Queen
        if (col == 4) board[{col, 0}] = 'K'; // King
    }

    // Set empty spaces for the rest of the board
    for (int col = 2; col < 6; ++col) {
        for (int row = 0; row < 8; ++row) {
            board[{row, col}] = ' '; // Empty space
        }
    }
}


void print_board(const map<pair<int, int>, char>& board) {
    // Print column headers
    cout << "  0 1 2 3 4 5 6 7\n";

    // Iterate through rows in reverse order (from 7 to 0)
    for (int row = 0; row <= 7; ++row) {
        cout << row << " "; // Print row number

        // Iterate through columns (from 0 to 7)
        for (int col = 0; col < 8; ++col) {
            auto it = board.find({col, row});
            if (it != board.end()) {
                cout << it->second << ' '; // Print the piece at (row, col)
            } else {
                cout << ". "; // Print '.' for empty space
            }
        }
        cout << '\n'; // Move to the next line after each row
    }
}

void print_map(const map<pair<int, int>, char>& board) {
    for (const auto& entry : board) {
        cout << "(" << entry.first.first << ", " << entry.first.second << ") -> " << entry.second << '\n';
    }
}

void print_moves_list(const map<char, vector<pair<pair<int, int>, pair<int, int>>>>& moves_list) {
    // Iterate over each key in the map
    for (const auto& p : moves_list) {
        char piece = p.first;
        const vector<pair<pair<int, int>, pair<int, int>>>& moves = p.second;

        cout << "Piece: " << piece << '\n';
        
        // Iterate over each move in the vector
        for (const auto& move : moves) {
            const auto& start = move.first;
            const auto& end = move.second;
            cout << "  From: (" << start.first << ", " << start.second << ") "
                      << "To: (" << end.first << ", " << end.second << ")\n";
        }
    }
}




int main() {

    map<pair<int, int>, char> board;
    initialize_board(board);
    map<pair<int, int>, char> prev_board = board;
    char player = 'w'; // Example character for player ('w' for white, 'b' for black)
    char opponent = 'b';
    vector<int> has_kings_moved;
    vector<int> has_rooks_moved;
    vector<pair<pair<int, int>, pair<int, int>>> can_passant; // Empty vector
    vector<pair<pair<int, int>, pair<int, int>>> castles; // Empty vector
    map<char, vector<pair<pair<int, int>, pair<int, int>>>> moves_list;
    tie(can_passant, moves_list) = check_en_passant(board, prev_board, moves_list, player);  
    tie(castles, moves_list) = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player);
    check_pawn(board, moves_list);
    check_knight(board, moves_list);
    check_bishop(board, moves_list);
    check_rook(board, moves_list);
    check_queen(board, moves_list);
    check_king(board, moves_list);

    while(true) {
        
        print_board(board);
        string move;
        cin >> move;
        pair<pair<int, int>, pair<int, int>> mov = parse_move(move);
        tie(can_passant, moves_list) = check_en_passant(board, prev_board, moves_list, player);
        
        tie(castles, moves_list) = check_castling(board, moves_list, has_kings_moved, has_rooks_moved, player);
        
        check_pawn(board, moves_list);
        check_knight(board, moves_list);
        check_bishop(board, moves_list);
        check_rook(board, moves_list);
        check_queen(board, moves_list);
        check_king(board, moves_list);
        
         // Example character for opponent ('b' for white, 'w' for black)
        bool check_promotion = false; // Example boolean
        prev_board = board;
        
        make_move(mov.first, mov.second, board, can_passant, castles, moves_list, player);
        
        moves_list = remove_illegal_moves(board, moves_list, castles, can_passant, player);
        moves_list = remove_illegal_moves(board, moves_list, castles, can_passant, opponent);
        player = (player == 'w') ? 'b' :'w';// Example character for player ('w' for white, 'b' for black)
        opponent = (player == 'w')? 'b' : 'w';
        

    }

    return 0;
    
}
