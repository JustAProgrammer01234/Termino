'''
All non courotine objects are here.
'''
import json

def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_help_fun():
    with open('txt files/help_fun.txt','r') as f:
        return f.read()

def get_help_mod():
    with open('txt files/help_moderation.txt','r') as f:
        return f.read()

def get_token():
    with open('txt files/token.txt','r') as f:
        return f.read()

def get_server_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def change_server_data(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent = 4)
