"""
Case 4
Developers: Kabaev A., Anufrienko K.
"""

# TODO


def run_command(command):
    if command == '1':
        dir_view()
    if command == '2':
        move_up()
    if command == '3':
        command_dir = input('Введите каталог, в который хотите перейти: ')
        move_down(command_dir)
    if command == '4':
        path = input('Введите каталог: ')
        count_files(path)
    if command == '5':
        path = input('Введите каталог: ')
        count_bytes(path)
    if command == '6':
        path = input('Введите каталог: ')
        target = input('Введите строку для поиска файла: ')
        find_files(target, path)
    if command == '7':
        exit()
    accept_command()


def dir_view():
    object_list = os.listdir(os.getcwd())
    files_list = []
    dir_list = []
    for _object in object_list:
        if _object.find('.') != -1:
            files_list.append(_object)
        else:
            dir_list.append(_object)
    print('Dirs:')
    for _dir in dir_list:
        print('\t' + _dir)
    print('Files:')
    for file in files_list:
        print('\t' + file)
    run_command(accept_command())


def move_up():
    path = os.getcwd()
    if path.count('\\') >= 1:
        path = path[:-path[::-1].find('\\') - 1]
    run_command(accept_command(path))


def move_down(command_dir):
    path = os.getcwd()
    if command_dir in os.listdir(path):
        path = f'{path}/{command_dir}'
    else:
        print('Некорректно введен подкатолог. ')
    run_command(accept_command(path))


def accept_command(path=os.getcwd()):
    os.chdir(path)
    print('-' * 50)
    print(f'{path}'' \n 1.Просмотр каталога \n 2.На уровень вверх \n 3.На уровень вниз \n' +
          ' 4.Количество файлов и каталогов \n' +
          ' 5.Размер текущего каталога(в байтах) \n 6.Поиск файла \n 7.Выход из программы')
    print('-' * 50)
    command = input('Выберите пункт меню: ')
    list_command = ['1', '2', '3', '4', '5', '6', '7']
    while command not in list_command:
        command = input('Введите корректный номер: ')
    return command


def main():
    run_command(accept_command())


if __name__ == '__main__':
    main()

# TODO
