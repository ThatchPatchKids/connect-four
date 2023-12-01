# Implement the minimax algorithm


game_board = [
        ['  ','  ','  ','  ','  ','  ','  '],        
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  ']
    ]


def evaluate(board):
    '''Evaluate the game state. Give a higher score to the maximizing player the more 
    pieces are in a row. Three in a row of your own chips should be a higher score than
    three in a row of the opponents chips.'''
    # 4 in a row = 4 points
    # 4 opponents in a row = -4 points
    # 3 in a row = 3 points
    # 3 opponenets in a row = -3 points
    score = 
    


def get_possible_moves(game_board):
    '''
    '''
    rows = [5,4,3,2,1,0]
    rows_i = 0
    cols = [0,1,2,3,4,5,6]
    cols_i = 0
    moves_list = []
    while cols_i < len(cols):
        spot = game_board[rows[rows_i]][cols[cols_i]]
        if spot.isspace():
            moves_list.append((rows[rows_i],cols[cols_i]))
            rows_i = 0
            cols_i += 1
        else:
            rows_i += 1
    return moves_list
        

# minimax algorithm:
# I have to make a copy of the current board, I cant just use the real board.
def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, maximizing_player)
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, maximizing_player)
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


game_board = [
        ['  ','  ','  ','  ','  ','  ','  '],        
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  ']
    ]


def game_over(board):
    # This func. is for determining terminal states 
    # I.e. when the game is over.

    # Could I use recursion to get the computer to check once with their chip and then a second time with players chips?
    # I could call it with a true and false to get it to change the chip and then finish the func.
    chip1 = '🐵'
    chip2 = '🔴'
    # Check row's for a win.
    for c in range(4):
        for r in range(6):
            if board[r][c] == chip1 and board[r][c+1] == chip1 and board[r][c+2] == chip1 and board[r][c+3] == chip1:
                return True
    # Check columns's for a win.
    for r in range(3):
        for c in range(7):
            if board[r][c] == chip1 and board[r][c+1] == chip1 and board[r][c+2] == chip1 and board[r][c+3] == chip1:
                return True
    # Check first diagonal for a win (how do you name each diagonal? Is there an official label for each?)
    
    # Check the second diagonal for a win. 


def make_move(board, move, maximizing_player, chip):
    '''
    '''
    if maximizing_player:
        chip = '🐵'
    else:
        chip = '🔴'
    row, col = move
    game_board[row][col] = chip
    return game_board


# get the best move func.
def get_best_move(board):
    best_move = None
    max_eval = float('-inf')
    for move in get_possible_moves(board):
        new_board = make_move(board, move, maximizing_player=True)
        eval = minimax(new_board, depth=3, maximizing_player=False)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

