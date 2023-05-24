import datetime

import mariadb

class Database:
    def __init__(self):
        self.connection = mariadb.connect(
            user=database_ids.user,
            password=database_ids.password,
            host=database_ids.host,
            port=database_ids.port,
            database=database_ids.database
        )
        self.cursor = self.connection.cursor()

    def find_token(self, token: str):
        query = "SELECT id_joueur, token, time FROM tokens WHERE token = ?"
        self.cursor.execute(query, (token,))
        result = self.cursor.fetchone()
        current_timestamp = datetime.datetime.now().timestamp()
        if result:
            if current_timestamp - result[2] < 20:
                return True, result[0]
            else:
                query = "DELETE FROM tokens WHERE token = ?"
                self.cursor.execute(query, (token,))
        return False, None
