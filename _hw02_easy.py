# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()
list_0 = ["яблоко", "банан", "киви", "арбуз"]
for s in list_0:
    print('{0}.{1:>7}'.format(list_0.index(s) + 1, s))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = ["яблоко", 11, "банан", "киви", 11, "арбуз", [3, 7, 21], "дыня", (1, 2)]
print("Первый список:", list_1)
list_2 = ["яблоко", (1, 2), "огурец", 12, "помидор", "виноград", 11, "дыня", "тыква"]
print("Второй список:", list_2)
for s in list_2:
    if s in list_1:
        count_of_s = list_1.count(s)
        while count_of_s != 0:
            list_1.remove(s)
            count_of_s -= 1
print("Первый список только с уникальными элементами:", list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list_3 = [76, 29, 22, 92, 79, 32, 72, 63, 16, 72]
print(list_3)
list_4 = []
for s in list_3:
    list_4.append(s / 4) if s % 2 == 0 else list_4.append(s * 2)
print(list_4)