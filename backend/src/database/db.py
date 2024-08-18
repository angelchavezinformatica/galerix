from mysql import connector

from config import CONFIG


class Database:
    def __init__(self) -> None:
        self.conn = connector.connect(
            user=CONFIG.get('DB_USER'),
            password=CONFIG.get('DB_PASSWORD'),
            host=CONFIG.get('DB_HOST'),
            port=CONFIG.get('DB_PORT'),
            database=CONFIG.get('DB_NAME'),
        )

    def server_info(self):
        if self.conn.is_connected():
            return self.conn.get_server_info()

    def select(self, sql: str, params: tuple = (), many=True):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)

        if many:
            return cursor.fetchall()
        return cursor.fetchone()

    def execute(self, sql: str, params: tuple = ()):
        cursor = self.conn.cursor()
        cursor.execute(sql, params)
        self.conn.commit()
        return cursor.lastrowid
