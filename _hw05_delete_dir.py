# Модуль удаления папки.

from os import getcwd, path
from shutil import rmtree


def delete_dir(dir_name):
    dir_path = path.join(getcwd(), dir_name)
    try:
        rmtree(dir_path)  # вместо os.rmdir() для удаления с содержимым
    except FileNotFoundError:
        print('Директория {} не существует'.format(dir_path))
    else:
        print('Директория {} удалена'.format(dir_path))
