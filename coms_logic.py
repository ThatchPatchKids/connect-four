# Author: Thatcher Albiston
from get_coords_and_check_winner import check_four_in_a_row


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


def test(moves_list):
    '''
    '''
    for move in moves_list:



def win_logic():
    '''
    '''



def move_near_logic():
    '''
    '''


def block_player_logic():
    '''
    '''


def eliminate_options():
    '''
    '''


