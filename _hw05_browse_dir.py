# Модуль, отображающий содержимое (в т.ч. только папки) текущей директории.

from os import getcwd, listdir, path


def browse_dir(only_dir=False):
    dir_path = getcwd()
    dir_list = listdir(dir_path)
    if only_dir:
        for d in dir_list[:]:
            if not (path.isdir(d)):
                dir_list.remove(d)
    if not (dir_list):
        dir_list = 'Директория {} пуста'.format(dir_path)
    return dir_list
