# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (с запросом подтверждения)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
    print('ping - тестовый ключ')


def make_dir():
    if not dir_or_file_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_or_file_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} создана'.format(dir_or_file_name))
    except FileExistsError:
        print('Директория {} уже существует'.format(dir_or_file_name))
    except FileNotFoundError:
        print('Указывайте только одну директорию')


def copy_file():
    if not dir_or_file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    if not os.path.isfile(dir_or_file_name):
        print('Файл {} не существует'.format(dir_or_file_name))
        return
    dir_path = os.path.join(os.getcwd(), dir_or_file_name)
    file_name = os.path.splitext(dir_or_file_name)
    copied_file = file_name[0] + '_copied' + file_name[1]
    shutil.copyfile(dir_or_file_name, copied_file)
    print('Файл {} скопирован'.format(dir_path))


def remove_file():
    if not dir_or_file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    if not os.path.isfile(dir_or_file_name):
        print('Файл {} не существует'.format(dir_or_file_name))
        return
    dir_path = os.path.join(os.getcwd(), dir_or_file_name)
    choice = input('Введите Y, чтобы подвердить удаление {} : '.format(dir_or_file_name))
    if choice in ('Y', 'y'):
        os.remove(dir_path)
        print('Файл {} удален'.format(dir_path))
    else:
        return


def change_dir():
    if not dir_or_file_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_or_file_name)
    try:
        os.chdir(dir_path)
        print('Текущая директория:', os.getcwd())
    except FileNotFoundError:
        print('Директория {} не существует'.format(dir_path))


def full_path_dir():
    print(os.getcwd())


def ping():
    print('pong')


do = {
    'help': print_help,
    'mkdir': make_dir,
    'cd': change_dir,
    'cp': copy_file,
    'rm': remove_file,
    'ls': full_path_dir,
    'ping': ping,
}

try:
    dir_or_file_name = sys.argv[2]
except IndexError:
    dir_or_file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')
