import json

def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_help_fun():
    with open('help/funcommands.txt','r') as f:
        return f.read()

def get_help_mod():
    with open('help/mod.txt','r') as f:
        return f.read()

def get_help_util_welcome():
    with open('help/utils/welcome.txt','r') as f:
        return f.read()

def get_help_util_mute():
    with open('help/utils/mute.txt','r') as f:
        return f.read()

def get_help_game():
    with open('help/games.txt') as f:
        return f.read()

def get_invite_link():
    with open('invitelink.txt') as f:
        return f.read()

def get_token(token_file):
    with open(token_file,'r') as f:
        return f.read()

def get_server_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def change_server_data(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent = 2)
