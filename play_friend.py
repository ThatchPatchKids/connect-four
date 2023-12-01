# New features, You can create an account with a players name and save data to them. Computer uses monkey and heart
# chips. If you beat computer easy then you get monkey chips if you beat hard you get heart chips unlocked and then
# computer uses random chips. 💖 🐵
# from is_winner import is_winner
from get_coords_and_check_winner import check_four_in_a_row

def play_friend(chips): 
    '''
    '''
    # Write a function to create this gameboard, then you can choose the size of the board.
    game_board = [
        ['  ','  ','  ','  ','  ','  ','  '],        
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  ']
    ]
    playing = True
    chip1, chip2 = choose_chips(chips)
    board = build_game_board(game_board)
    print(board)
    while playing:
        msg, chip = decide_turn(game_board, chip1, chip2)
        print(msg)
        coords = make_a_move(game_board)
        game_board = drop_chip_in_board(chip, coords, game_board)
        build_game_board(game_board)
        if check_four_in_a_row(coords, chip, game_board):
            playing = False
    if chip == chip1:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')


def choose_chips(chips):
    '''
    '''
    print('Choose your chip pieces: ')
    for i in range(len(chips)):
        print(f'{i + 1}) {chips[i]}')

    print('\nPlayer 1, go!')
    chip1 = int(input('   > '))
    for i in range(len(chips)+1):
        if i == chip1:
            chip1 = chips[i-1]

    print('Player 2, go!')  
    chip2 = int(input('   > '))
    for i in range(len(chips)+1):
        if i == chip2:
            chip2 = chips[i-1]
    return chip1, chip2


def build_game_board(game_board):
    '''
    '''
    for i in range(len(game_board)):
        print("+---+---+---+---+---+---+---+")
        for j in range(len(game_board[i])):
            print(f"| {game_board[i][j]}" ,end="")
        print('|')
    

def decide_turn(game_board, chip1, chip2):
    '''
    '''
    space_count = 0
    for row in game_board:
        space_count += row.count('  ')
    if space_count % 2 == 0:
        msg = 'Player 1, GO!'
        chip = chip1
    else:
        msg = 'Player 2, GO!'
        chip = chip2
    return msg, chip


def make_a_move(game_board):
    '''
    '''
    print('Choose a column')
    column = int(input('    > '))

    rows = [0,1,2,3,4,5]
    for row in reversed(rows):
        # Get the spot index.
        spot = game_board[row][column-1]
        
        # Is the spot empty?
        if spot.isspace():
            return (row, column-1)


def drop_chip_in_board(chip, coords, game_board):
    '''
    '''
    row, column = coords
    game_board[row][column] = chip
    return game_board


