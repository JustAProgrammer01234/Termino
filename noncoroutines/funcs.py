import json

def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_help_fun():
    with open('cmdlist/funcommands.txt','r') as f:
        return f.read()

def get_help_mod():
    with open('cmdlist/mod.txt','r') as f:
        return f.read()

def get_help_util_welcome():
    with open('cmdlist/settings/welcome.txt','r') as f:
        return f.read()

def get_help_util_mute():
    with open('cmdlist/settings/mute.txt','r') as f:
        return f.read()

def get_help_game():
    with open('cmdlist/games.txt') as f:
        return f.read()

def get_invite_link():
    with open('invitelink.txt') as f:
        return f.read()

def get_json_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def change_json_data(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent = 2)
