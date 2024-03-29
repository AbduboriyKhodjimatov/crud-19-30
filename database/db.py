import sqlite3


def connect(db_name: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor
