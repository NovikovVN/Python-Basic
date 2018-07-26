# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
from random import randint


class Person:
    def __init__(self):
        self.name = 'random person'
        self.health = randint(95, 130)
        self.damage = randint(8, 10)
        self.armor = randint(8, 20) / 10

    def _damaged(self, damage):
        return int(damage / self.armor)

    def attacked(self, name, damage):
        self.health -= self._damaged(damage)
        print('{} наносит {} урона. {} имеет {} здоровья.'.format(name, damage, self.name, self.health))


class Player(Person):
    def __init__(self):
        super().__init__()
        self.name = input('Введите Ваше имя: ')


class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.name = input('Вызовите противника: ')


class Game:
    def start(self):
        player = Player()
        enemy = Enemy()
        order = randint(0, 1)
        while player.health > 0 and enemy.health > 0:
            if order:
                player.attacked(enemy.name, enemy.damage)
                order = 0
            else:
                enemy.attacked(player.name, player.damage)
                order = 1
        if player.health > 0:
            print('{} победил!'.format(player.name))
        else:
            print('{} победил!'.format(enemy.name))


game = Game()
game.start()