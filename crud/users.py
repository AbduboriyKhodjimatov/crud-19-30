from database.db import connect


class UserService:
    connection, cursor = connect('todos.db')
    def __check_user_exists(self, **kwargs):
        sql = 'SELECT id FROM users WHERE user_name =?;'
        self.cursor.execute(sql, (kwargs['user_name'],))
        user_id = self.cursor.fetchone()
        if user_id:
            return True
        return False

    def create(self, **kwargs):
        if self.__check_user_exists(user_name=kwargs['user_name']):
            print('There is such user')
            return
        sql = 'INSERT INTO users(user_name) VALUES (?)'
        self.cursor.execute(sql, (kwargs['user_name'],))
        self.connection.commit()
        print('Добавили', kwargs['user_name'])

    def read(self, **kwargs): # all = True
        sql = 'SELECT * FROM users;'
        users = self.cursor.execute(sql).fetchall()
        return users

    def update(self, **kwargs):
        sql = 'UPDATE users SET user_name = ? WHERE user_name = ?'
        self.cursor.execute(sql, (kwargs['new_user_name'],kwargs['user_name'] ))
        self.connection.commit()
        print(f'Изменили имя {kwargs["user_name"]}')

    def delete(self, **kwargs):
        sql = 'DELETE FROM users WHERE user_name = ?'
        self.cursor.execute(sql, (kwargs['user_name'],))
        self.connection.commit()
        print(f'Удалили пользователя с именем {kwargs["user_name"]}')
