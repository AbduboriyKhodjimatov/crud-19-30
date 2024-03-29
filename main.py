from crud.users import UserService

user_service = UserService()
while True:

    command = input('1.users\n2.todos\ncommand: ')
    if command == 'users':
        crud_commands = '\n'.join(['1.create', '2.read', '3.update', '4.delete'])
        crud_command = input(f'{crud_commands}\nВыберите цифру: ')
        if crud_command == '1':
            print('create')
            user_name = input('user_name: ')
            user_service.create(user_name=user_name)
        elif crud_command == '2':
            print('read')
            users = user_service.read()
            for user_id, user_name in users:
                print(f'''==========
ID: {user_id} 
USER_NAME: {user_name}
''')
        elif crud_command == '3':
            print('update')
            users = [user_name for _, user_name in user_service.read()]
            users_names = '\n'.join([f'{idx}. {user_name}' for idx, user_name in enumerate(users, start=1)])
            user_name = input(f'{users_names}\n Введите имя для изменения: ')
            new_user_name = input('Введите новое имя: ')
            user_service.update(new_user_name = new_user_name, user_name = user_name)
        elif crud_command == '4':
            print('delete')
            users = [user_name for _, user_name in user_service.read()]
            users_names = '\n'.join([f'{idx}. {user_name}' for idx, user_name in enumerate(users, start=1)])
            name_for_delete = input(f'{users_names}\n Напишите имя для удаления: ')
            user_service.delete(user_name=name_for_delete)

    elif command == 'todos':
        pass
    else:
        print('Такой команды нет, выберите из двух данных ниже:')