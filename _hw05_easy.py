# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.

import _hw05_create_dir as cd

dir_1_9 = ['dir_{}'.format(i) for i in range(1, 10)]
for d in dir_1_9:
    cd.create_dir(d)

# И второй скрипт, удаляющий эти папки.

import _hw05_delete_dir as dd

dir_1_9 = ['dir_{}'.format(i) for i in range(1, 10)]
for d in dir_1_9:
    dd.delete_dir(d)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import _hw05_browse_dir as bd

print(bd.browse_dir(only_dir=True))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import _hw05_copy_file
