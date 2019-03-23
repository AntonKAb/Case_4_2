"""
Case 4
Developers: Kabaev A., Anufrienko K.
"""
import os

# TODO


# TODO
def count_files(path):
    objects_list = os.listdir(f'{os.getcwd()}/{path}')
    names_sum = ''
    for _object in objects_list:
        names_sum += _object
    if names_sum.count('.') == len(objects_list):
        return len(objects_list)
    files_list = []
    dir_list = []
    for _object in objects_list:
        if _object.find('.') != -1:
            files_list.append(_object)
        else:
            dir_list.append(_object)
    inside_files = 0
    for _dir in dir_list:
        inside_files += count_files(f'{path}/{_dir}')
    return len(files_list) + inside_files


def count_bytes(path):
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


def find_files(target, path):
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
    inside_files = []
    for _dir in dir_list:
        inside_files += find_files(target, f'{path}/{_dir}')
    targets_files = []
    for file in files_list:
        if file.find(target) != -1:
            targets_files.append(f'{os.getcwd()}/{path}/{file}')
    if names_sum.count('.') == objects_list:
        return targets_files
    return targets_files + inside_files
