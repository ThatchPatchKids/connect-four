
from play_computer import play_computer
from play_friend import play_friend
from user_info import login, create_acct, get_chips, get_board, save_user_info, get_user_info


def play_game():
    '''
    '''
    # 
    decision = welcome_user()

    # 
    if decision == '1':
        # 
        username, users_dicts, chips = login()
    # 
    elif decision == '2':
        # 
        username, users_dicts = create_acct()
        # 
        path = save_user_info(users_dicts)
        # 
        chips = get_chips(username, users_dicts)
        
    else:
        # 
        print('Sorry, thats not an option.')

    # 
    if not load_game():
        new_game(chips)
    else:
        board = get_board()


def welcome_user():
    '''
    '''
    print('Welcome to Connect Four!')
    print('''
1. Login
2. Create Account
''', end='')
    decision = input('  > ')
    return decision


def load_game():
    '''
    '''
    print('''Do you wish to load game?
1. Yes
2. No''')
    decision = input('  > ')
    if decision == '1':
        return True
    else:
        return False


def new_game(chips):
    '''
    '''
    print('''
1. Play a Friend
2. Play the Easy Computer
3. Play the Hard Computer''')
    decision = input('  > ')
    if decision == '1':
        play_friend(chips)
    elif decision == '2':
        play_computer
    else:
        play_computer


if __name__ == '__main__':
    play_game()

