# 
import random
from get_coords_and_check_winner import check_four_in_a_row


def play_computer(chips):
    '''
    '''
    game_board = [
        ['  ','  ','  ','  ','  ','  ','  '],        
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  '],     
        ['  ','  ','  ','  ','  ','  ','  ']
    ]
    playing = True
    chip = choose_chips(chips)
    board = build_game_board(game_board)
    print(board)
    while playing:
        # Whos turn is it? 
        # Print a message with the username for players turn
        # Print a message when the computer plays.
        coords = is_valid_move(game_board)
        game_board = drop_chip_in_board(chip, coords, game_board)
        build_game_board(game_board)
        if check_four_in_a_row(coords, chip, game_board):
            playing = False
    if chip:
        print('Player 1 wins!')
    else:
        print('Computer wins!')


def choose_chips(username, chips):
    '''
    '''
    print('Choose your chip pieces: ')
    for i in range(len(chips)):
        print(f'{i + 1}) {chips[i]}')
    print(f'\n{username}, go!')
    chip = int(input('   > '))

    for i in range(len(chips)+1):
        if i == chip:
            chip = chips[i-1]
    return chip


def build_game_board(game_board):
    '''
    '''
    for i in range(len(game_board)):
        print("+---+---+---+---+---+---+---+")
        for j in range(len(game_board[i])):
            print(f"| {game_board[i][j]}" ,end="")
        print('|')


def is_valid_move(game_board, player, col):
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


def easy_coms_move(player_coords, player_chip, game_board):
    '''
    '''
    chip = '💖'
    row, column = player_coords


def hard_coms_move():
    '''
    '''
    chip = '🐵'


def mirror_player(game_board):
    '''
    '''
    rows = [0,1,2,3,4,5]
    cols = [0,1,2,3,4,5,6]
    if game_board.count('  ') > 1:
        col = random(cols)
        make_a_move(col)