# Author: Thatcher Albiston
# Change the fours into a variable and depending on whether its the cpu or the player change from 3 or 4.


def possible_vert_coords(coords, in_a_row):
    '''
    '''
    row, col = coords
    # Save the rows starting coord to reset it later.
    row_start = row

    # Move up the board to get possible winning coords.
    up = []
    up.append(coords)
    while row > 0 and len(up) != in_a_row:
        row -= 1
        assert row >= 0
        assert row != row_start
        up.append((row, col))
    if len(up) < in_a_row and len(up) != in_a_row:
        row = row_start
        while row < 5 and len(up) != in_a_row:
            row += 1
            assert row <= 5
            assert row != row_start
            up.append((row, col))
    
    # Move down the board to get possible winning coords.
    row = row_start
    down = []
    down.append(coords)
    while row < 5 and len(down) != in_a_row:
        row += 1
        assert row <= 5
        assert row != row_start
        down.append((row, col))
    if len(down) < in_a_row and len(down) != in_a_row:   # Is the != 4 necessary? No matter what it needs to be less than 4 right? 
        row = row_start
        while row > 0 and len(down) != in_a_row:
            row -= 1
            assert row >= 0
            assert row != row_start
            down.append((row, col))
    # Return a list of the moves lists.
    assert len(up) <= in_a_row
    assert len(down) <= in_a_row
    return [up, down]


def possible_horiz_coords(coords, in_a_row):
    '''
    '''
    row, col = coords
    col_start = col
    
    # Move to the right of the board for possible wins.
    right = []
    right.append(coords)
    while col < 6 and len(right) != in_a_row:
        col += 1
        assert col <= 6
        assert col != col_start
        right.append((row, col))
    if len(right) < in_a_row and len(right) != in_a_row:
        col = col_start
        while col > 0 and len(right) != in_a_row:
            col -= 1
            assert col >= 0
            assert col != col_start
            right.append((row, col))

    # Move to the left of the board for possible wins.
    left = []
    left.append(coords)
    col = col_start
    while col > 0 and len(left) != in_a_row:
        col -= 1
        assert col >= 0
        assert col != col_start
        left.append((row, col))
    if len(left) < in_a_row and len(left) != in_a_row:
        col = col_start
        while col < 6 and len(left) != in_a_row:
            col += 1
            assert col <= 6
            assert col != col_start
            left.append((row, col))
    
    # Return a list of moves lists.
    # print(right)
    # print(left)
    assert len(right) <= in_a_row
    assert len(left) <= in_a_row
    return [right, left]


def possible_diags_coords1(coords, in_a_row):
    '''
    '''
    row, col = coords
    row_start = row
    col_start = col

    # Move diagonally up to the right to find possible winning moves.
    up_diag = []
    up_diag.append(coords)
    while row > 0 and col < 6 and len(up_diag) != in_a_row:
        row, col = row - 1, col + 1
        assert row >= 0 and col <= 6
        assert row != row_start and col != col_start
        up_diag.append((row, col))
    if len(up_diag) < in_a_row and len(up_diag) != in_a_row:
        row, col = row_start, col_start
        while row < 5 and col > 0 and len(up_diag) != in_a_row:
            row, col = row + 1, col - 1
            assert row <= 5 and col >= 0
            assert row != row_start and col != col_start
            up_diag.append((row, col))
    
    row, col = row_start, col_start
    # Move diagonally down to the left to find possible winning moves.
    down_diag = []
    down_diag.append(coords)
    while row < 5 and col > 0 and len(down_diag) != in_a_row:
        row, col = row + 1, col - 1
        assert row <= 5 and col >= 0
        assert row != row_start and col != col_start
        down_diag.append((row, col))
    if len(down_diag) < in_a_row and len(down_diag) != in_a_row:
        row, col = row_start, col_start
        while row > 0 and col < 6 and len(down_diag) != in_a_row:
            row, col = row - 1, col + 1
            assert row >= 0 and col <= 6
            assert row != row_start and col != col_start
            down_diag.append((row, col))
    assert len(up_diag) <= in_a_row
    assert len(down_diag) <= in_a_row
    return [up_diag, down_diag]


def possible_diags_coords2(coords, in_a_row):
    '''
    '''
    row, col = coords
    row_start = row
    col_start = col

    # Move diagonally up to the left to find possible winning moves.
    up_diag = []
    up_diag.append(coords)
    while row > 0 and col > 0 and len(up_diag) != in_a_row:
        row, col = row - 1, col - 1
        assert row >= 0 and col >= 0
        assert row != row_start and col != col_start
        up_diag.append((row, col))
    if len(up_diag) < in_a_row and len(up_diag) != in_a_row:
        row, col = row_start, col_start
        while row < 5 and col < 6 and len(up_diag) != in_a_row:
            row, col = row + 1, col + 1
            assert row <= 5 and col <= 6
            assert row != row_start and col != col_start
            up_diag.append((row, col))
    
    row, col = row_start, col_start
    # Move diagonally down to the right to find possible winning moves.
    down_diag = [] 
    down_diag.append(coords)
    while row < 5 and col < 6 and len(down_diag) != in_a_row:
        row, col = row + 1, col + 1
        assert row <= 5 and col <= 6
        assert row != row_start and col != col_start
        down_diag.append((row, col))
    if len(up_diag) < in_a_row and len(up_diag) != in_a_row:
        row, col = row_start, col_start
        while row > 0 and col > 0 and len(down_diag) != in_a_row:
            row, col = row - 1, col - 1
            assert row >= 0 and col >= 0
            assert row != row_start and col != col_start
            down_diag.append((row, col))
    # print(up_diag)
    # print(down_diag)
    assert len(up_diag) <= in_a_row
    assert len(down_diag) <= in_a_row
    return [up_diag, down_diag]


def create_moves_list(coords, in_a_row):
    '''
    '''

    possible_moves = []
    for func in [possible_vert_coords, possible_horiz_coords, possible_diags_coords1, possible_diags_coords2]:
        result = func(coords, in_a_row)
        possible_moves.append(result)
    return possible_moves


def check_four_in_a_row(coords, chip, game_board, player=''):
    '''
    '''
    if player == "cpu's move":
        in_a_row = 3
    else:
        in_a_row = 4
    possible_moves = create_moves_list(coords, in_a_row)   
    i = 0
    while i < 4:
        for possible in possible_moves[i]:
            win = 0
            for move in possible:
                row = move[0]
                col = move[1]
                if game_board[row][col] == chip:
                    win += 1
                if game_board[row][col] != chip:
                    win = 0
                if win == 4:
                    return True
        i += 1
    return False