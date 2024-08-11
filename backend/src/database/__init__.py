from mysql import connector

from config import CONFIG

CONN = connector.connect(
    user=CONFIG.get('DB_USER'),
    password=CONFIG.get('DB_PASSWORD'),
    host=CONFIG.get('DB_HOST'),
    port=CONFIG.get('DB_PORT'),
    database=CONFIG.get('DB_NAME'),
)
