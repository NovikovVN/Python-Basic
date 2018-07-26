# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class ToyCroc:
    def __init__(self):
        self.name = 'Крокодил'
        self.color = 'зеленый'
        self.line = 'Животные Африки'

    def resource_bying(self):
        print('Закуплено базовое сырье')

    def factory_sewing(self):
        print('Пошив общего качества')

    def factory_painting(self):
        print('Покраска общего качества')


crocodile = ToyCroc()
print(crocodile.color)
print(crocodile.name)
crocodile.factory_painting()


class ToyGena:
    def __init__(self):
        self.name = 'Крокодил Гена'
        self.color = 'зеленый, коричневый'
        self.line = 'Союзмультфильм'

    def resource_bying(self):
        print('Закуплено сырье высокого качетсва')

    def factory_sewing(self):
        print('Пошив общего качества с контролем')

    def factory_painting(self):
        print('Покраска общего качества с контролем')


crocodile_gena = ToyGena()
print(crocodile_gena.color)
print(crocodile_gena.name)
crocodile_gena.factory_painting()


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, toy_name, toy_color, toy_line):
        self.name = toy_name
        self.color = toy_color
        self.line = toy_line


class ToyAnimal(Toy):
    def __init__(self, toy_name, toy_color, toy_line):
        super().__init__(toy_name, toy_color, toy_line)

    def resource_bying(self):
        print('Закуплено базовое сырье')

    def factory_sewing(self):
        print('Пошив общего качества')

    def factory_painting(self):
        print('Покраска общего качества')


class ToyCartoon(Toy):
    def __init__(self, toy_name, toy_color, toy_line):
        super().__init__(toy_name, toy_color, toy_line)

    def resource_bying(self):
        print('Закуплено сырье высокого качетсва')

    def factory_sewing(self):
        print('Пошив общего качества с контролем')

    def factory_painting(self):
        print('Покраска общего качества с контролем')


class Factory:
    def make_toy(self):
        toy_line = input('Какую серии вы хотите? ')
        if not (toy_line in ('Крокодил', 'Бегемот', 'Попугай') or toy_line in (
        'Marvel', 'DC', 'Disney', 'Союзмультфильм')):
            print('К сожалению, данной серии нет')
            return None
        toy_name = input('Введите название игрушки из серии:')
        toy_color = input('Введите цвет игрушки из серии:')
        if toy_line in ('Крокодил', 'Бегемот', 'Попугай'):
            toy = ToyAnimal(toy_name, toy_color, toy_line)
        elif toy_line in ('Marvel', 'DC', 'Disney', 'Союзмультфильм'):
            toy = ToyCartoon(toy_name, toy_color, toy_line)
        return toy


f = Factory()
toy = f.make_toy()
if toy:
    print('Название игрушки: ', toy.name)
    print('Цвет игрушки: ', toy.color)
    print('Серия: ', toy.line)
    print('Закупленное сырьё: ', end='')
    toy.resource_bying()
    print('Пошив: ', end='')
    toy.factory_sewing()
    print('Покрас: ', end='')
    toy.factory_painting()