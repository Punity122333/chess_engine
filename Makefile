# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

# Target executable name
TARGET = chess_engine

# Source files (located in chessEngineCPP directory)
SRCS = ChessEngine/chessEngineCPP/bishop.cpp \
       ChessEngine/chessEngineCPP/castles.cpp \
       ChessEngine/chessEngineCPP/chess.cpp \
       ChessEngine/chessEngineCPP/illegal_removal.cpp \
       ChessEngine/chessEngineCPP/king.cpp \
       ChessEngine/chessEngineCPP/knight.cpp \
       ChessEngine/chessEngineCPP/move.cpp \
       ChessEngine/chessEngineCPP/parser.cpp \
       ChessEngine/chessEngineCPP/pawn.cpp \
       ChessEngine/chessEngineCPP/queen.cpp \
       ChessEngine/chessEngineCPP/rook.cpp \
       ChessEngine/chessEngineCPP/specialmoves.cpp \
       ChessEngine/chessEngineCPP/utility.cpp

# Object files (same as SRCS but with .o instead of .cpp)
OBJS = $(SRCS:.cpp=.o)

# Default rule to build the target
all: $(TARGET)

# Link object files to create executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Rule to compile .cpp files into .o files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean rule to remove object files and executable
clean:
	rm -f $(OBJS) $(TARGET)
