import os
from bot import termino

if __name__ == '__main__':
    termino.load_extension('bot')
    termino.load_extension('helpcommand')
    for content in os.listdir():
        if os.path.isdir(content) and content not in ['noncoroutines','cmdlist', '__pycache__'] and not content.startswith('.'):
            termino.load_extension(content)
    termino.run(os.getenv('TOKEN'))