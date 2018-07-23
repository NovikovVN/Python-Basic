# Модуль создания папки.

from os import getcwd, mkdir, path


def create_dir(dir_name):
    dir_path = path.join(getcwd(), dir_name)
    try:
        mkdir(dir_path)
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_path))
    else:
        print('Директория {} создана'.format(dir_path))
