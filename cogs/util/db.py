import asyncpg 

class DataBase:
    def __init__(self, user, passwd, host, port):
        self.user = user 
        self.passwd = passwd 
        self.host = host 
        self.port = port 