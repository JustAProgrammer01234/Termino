import os
from bot import termino
from noncoroutines import get_token

if __name__ == '__main__':
    termino.load_extension('bot')
    termino.load_extension('helpcommand')
    for content in os.listdir():
        if os.path.isdir(content) and content not in ['noncoroutines','cmdlist', '__pycache__']:
            termino.load_extension(content)
    termino.run(get_token('token.txt'))