class TerminoDbClient:
    def __init__(self, user, passwd, host, port, database):
        self.pool = None
        self.dsn = f'postgres://{user}:{passwd}@{host}:{port}/{database}'  