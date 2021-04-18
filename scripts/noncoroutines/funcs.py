'''
All non courotine objects are here.
'''
import time

def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_token():
    with open('txt files/token.txt','r') as f:
        return f.read()
