alphdict = {'a':0,'b':1, 'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
def parse_coordinate(coord: str) -> tuple:
    """
    The function `parse_coordinate` takes a string representing a chess coordinate and returns a tuple
    with the corresponding numerical coordinates.
    
    :param coord: The `coord` parameter is a string representing a coordinate on a chess board. It
    typically consists of a letter (from 'a' to 'h') representing the column and a number (from 1 to 8)
    representing the row
    :type coord: str
    :return: The function `parse_coordinate` takes a string `coord` as input, which represents a chess
    coordinate in the format "letternumber" (e.g., "a1", "h8"). The function then returns a tuple
    containing the corresponding numerical coordinates in the format (x, y), where x represents the
    column (0-7) and y represents the row (0-7) on a
    """
    return (alphdict[coord[0]], 7 - (int(coord[1]) - 1))

def parse_move(mov: str) -> tuple:
    """
    The function `parse_move` takes a string representing a chess move and returns a tuple of the
    starting and ending coordinates of the move after parsing.
    
    :param mov: The `mov` parameter is a string representing a chess move. It consists of four
    characters where the first two characters represent the starting position of a piece on a
    chessboard, and the last two characters represent the ending position of the piece after the move
    :type mov: str
    :return: The `parse_move` function is returning a tuple containing the start and end coordinates of
    a move.
    """
    
    mov = list(mov)
    start = parse_coordinate(mov[0] +mov[1])
    end = parse_coordinate(mov[2] + mov[3])
    return (start, end)