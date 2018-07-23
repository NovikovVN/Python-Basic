# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
from _hw05_create_dir import create_dir
from _hw05_delete_dir import delete_dir
from _hw05_browse_dir import browse_dir

while True:
    try:
        choice = int(input('Выберите пункт:\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           '---------------------\n'
                           'Ваш выбор: '))
        if choice == 1:
            try:
                dir_name = input('Введите имя папки или путь для перехода: ')
                dir_path = os.path.join(os.getcwd(), dir_name)
                os.chdir(dir_path)
                print('Текущая директория:', os.getcwd())
            except FileNotFoundError:
                print('Директория {} не существует'.format(dir_path))
        elif choice == 2:
            print('Содержимое директории:', os.getcwd())
            print(browse_dir())
        elif choice == 3:
            dir_name = input('Введите имя удаляемой папки: ')
            delete_dir(dir_name)
        elif choice == 4:
            dir_name = input('Введите имя создаваемой папки: ')
            create_dir(dir_name)
        elif choice == 5:
            break
        elif not (choice in (1, 2, 3, 4)):
            print('Опция {} не поддерживается'.format(choice))
    except ValueError:
        print('Пожалуйста, вводите только числа')