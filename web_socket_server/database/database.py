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
        password = hashlib.sha256(password.encode()).hexdigest()
        query = "INSERT INTO users (name, password) VALUES (?, ?)
        self.cursor.execute(query, (username, password))
        self.connection.commit()