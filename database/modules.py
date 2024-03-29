from database.db import connect

class DBTableCreator:
    def __init__(self):
        self.connection, self.cursor = connect('../todos.db')


    def create_users_table(self):
        sql = ''' DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT UNIQUE
        );
        
        
        '''
        self.cursor.executescript(sql)
        self.connection.commit()
        print('создали таблицу users')

    def create_todos_table(self):
        sql_1 = ''' DROP TABLE IF EXISTS todos;
        CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id),
        title TEXT UNIQUE,
        description TEXT,
        is_finished BOOLEAN, 
        created_at TEXT
        );


        '''
# BOOLEAN  возвращает TRUE OR FALSE
        self.cursor.executescript(sql_1)
        self.connection.commit()
        print('создали таблицу todos')


# creator = DBTableCreator()
# creator.create_users_table()
# creator.create_todos_table()





