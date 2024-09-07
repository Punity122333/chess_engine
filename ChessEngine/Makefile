# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -g

# Target executable name
TARGET = chess_engine

# Source files (located in chessEngineCPP directory)
SRCS = chessEngineCPP/bishop.cpp \
       chessEngineCPP/castles.cpp \
       chessEngineCPP/chess.cpp \
       chessEngineCPP/engine.cpp \
       chessEngineCPP/illegal_removal.cpp \
       chessEngineCPP/king.cpp \
       chessEngineCPP/knight.cpp \
       chessEngineCPP/move.cpp \
       chessEngineCPP/parser.cpp \
       chessEngineCPP/pawn.cpp \
       chessEngineCPP/queen.cpp \
       chessEngineCPP/rook.cpp \
       chessEngineCPP/specialmoves.cpp

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
