# chess_engine

A chess game in Python, complete with UI/UX and all the rules, including checkmate, all possible possiblities of stalemate, en passant and castling.

# About the Engine

The Chess engine is in development and will be uploaded once the first prototype is done.

# Dependencies (Python):

pygame for the UI/UX rendering.
Install using 

```py
pip install pygame
```
# Dependencies (C++):

Have MinGW installed and configured properly. To run the C++ part of the program, run:

```powershell
g++ -std=c++17 -o ../chess.exe chess.cpp pawn.cpp knight.cpp bishop.cpp rook.cpp queen.cpp king.cpp illegal_removal.cpp move.cpp parser.cpp specialmoves.cpp utility.cpp castles.cpp -mconsole
```


