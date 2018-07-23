# Модуль копирования файла.

import os
import sys
import shutil

if __name__ != '__main__':
    origin_file = sys.argv[0]
    file_name = os.path.splitext(origin_file)
    copied_file = file_name[0] + '_copied' + file_name[1]
    shutil.copyfile(origin_file, copied_file)
    print('Файл {} скопирован!'.format(origin_file))
