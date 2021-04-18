'''
All non courotine objects are here.
'''
def get_help():
    with open('txt files/help.txt','r') as f:
        return f.read()

def get_token():
    with open('txt files/token.txt','r') as f:
        return f.read()
