import os 
import json

usernames = []
users_dicts = []


def login():
    '''
    '''
    logging_in = True
    while logging_in:
        username = input('Whats your username? ')
        users_dicts = get_user_info()
        chips = get_chips(username, users_dicts)
        if chips is not None:
            logging_in = False
        else:
            print('Sorry, Incorrect Username.')
    return username, users_dicts, chips


def get_user_info(path='cse111\\week-13\\final-Connect-Four\\chips.json'):
    '''
    '''
    try:
        with open(path) as json_file:
            users_dicts = json.load(json_file)
    except FileNotFoundError:
        print('Sorry, User Info not gathered.')
    return users_dicts


def save_user_info(users_dicts, path='cse111\\week-13\\final-Connect-Four\\chips.json'):
    '''
    '''
    # path[:0] += username    # when path='.json', would it work?
    try:
        with open(path, 'w') as json_file:
            json.dump(users_dicts, json_file)
    except:
        print('Info not saved')
    return path


def create_acct(chips=['🔴','⚪','⚫','🟤','🟣','🔵','🟢','🟡','🟠', '*', '*'], users_dicts=get_user_info()):
    username = input('Whats your username? ')
    usernames.append(username)
    users_dicts.append({"username": username, "chips": chips})
    return username, users_dicts


def get_chips(username, users_dicts):
    for user in users_dicts:
        if user["username"] == username:
            return user["chips"]


def get_board(username):
    '''
    '''
    path = get_path()
    with open(path, 'r') as file:
        txt = file.read()
        data = json.loads(txt)
        board = data["gameboard"]
    return board


def save_game(game_board):
    '''
    '''
    path = get_path()
    try:
        with open(path, 'w') as json_file:
            json.dump(game_board, json_file)
    except:
        print('Info not saved.')


def get_path(username):
    '''
    '''
    path = username + '.json'
    return path
