"""
Case 4
Developers: Kabaev A., Anufrienko K.
"""
import os


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


def move_up():
    path = os.getcwd()
    if path.count('\\') >= 1:
        path = path[:-path[::-1].find('\\') - 1]
    os.chdir(path)
    run_command(accept_command(path))


def move_down(command_dir):
    path = os.getcwd()
    if command_dir in os.listdir(path):
        path = f'{path}/{command_dir}'
    else:
        print('Некорректно введен подкатолог. ')
    os.chdir(path)
    run_command(accept_command(path))


def count_files(path):
    try:
        objects_list = os.listdir(f'{os.getcwd()}/{path}')
        names_sum = ''
        for _object in objects_list:
            names_sum += _object
        if names_sum.count('.') == len(objects_list):
            return len(objects_list)
        dir_list = []
        for _object in objects_list:
            if _object.find('.') == -1:
                dir_list.append(_object)
        inside_files = 0
        for _dir in dir_list:
            inside_files += count_files(f'{path}/{_dir}')
        return len(objects_list) + inside_files
    except FileNotFoundError:
        print(f'Папка {path} не найдена')
    except NotADirectoryError:
        pass


def count_bytes(path):
    try:
        objects_list = os.listdir(f'{os.getcwd()}/{path}')
        names_sum = ''
        for _object in objects_list:
            names_sum += _object
        files_list = []
        dir_list = []
        for _object in objects_list:
            if _object.find('.') != -1:
                files_list.append(_object)
            else:
                dir_list.append(_object)
        inside_files = 0
        for _dir in dir_list:
            inside_files += count_bytes(f'{path}/{_dir}')
        bytes_sum = 0
        for file in files_list:
            bytes_sum += os.stat(f'{os.getcwd()}/{path}/{file}').st_size
        if names_sum.count('.') == objects_list:
            return bytes_sum
        return bytes_sum + inside_files
    except FileNotFoundError:
        print(f'Папка {path} не найдена')
    except NotADirectoryError:
        pass


def find_files(target, path):
    try:
        objects_list = os.listdir(f'{os.getcwd()}/{path}')
        names_sum = ''
        for _object in objects_list:
            names_sum += _object
        files_list = []
        dir_list = []
        for _object in objects_list:
            if _object.find('.') != -1:
                files_list.append(_object)
            else:
                dir_list.append(_object)
        inside_files = ''
        for _dir in dir_list:
            inside_files += find_files(target, f'{path}/{_dir}')
        targets_files = ''
        for file in files_list:
            if file.find(target) != -1:
                targets_files += f'{os.getcwd()}/{path}/{file}\n'
        if names_sum.count('.') == objects_list:
            return targets_files
        return targets_files + inside_files
    except FileNotFoundError:
        print(f'Папка {path} не найдена')
    except NotADirectoryError:
        pass

  
def accept_command(path):
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

  
def run_command(command):
    if command == '1':
        dir_view()
        run_command(accept_command(os.getcwd()))
    if command == '2':
        move_up()
    if command == '3':
        command_dir = input('Введите каталог, в который хотите перейти: ')
        move_down(command_dir)
    if command == '4':
        path = input('Введите каталог: ')
        print(f'Внутри содержится {count_files(path)} файл(ов)')
        run_command(accept_command(os.getcwd()))
    if command == '5':
        path = input('Введите каталог: ')
        print(f'Папка {path} весит {count_bytes(path)} байтов.')
        run_command(accept_command(os.getcwd()))
    if command == '6':
        path = input('Введите каталог: ')
        target = input('Введите строку для поиска файла: ')
        print(f'В папке {path} найдены следующие файлы с {target} в названии: \n{find_files(target, path)}')
        run_command(accept_command(os.getcwd()))
    if command == '7':
        exit()
  

def main():
    run_command(accept_command(os.getcwd()))


if __name__ == '__main__':
    main()
