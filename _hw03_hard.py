# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

PlayerName = input('Введите имя игрока: ')
EnemyName = input('Введите имя противника: ')

player = {'name': PlayerName, 'health': 135, 'damage': 9}
enemy = {'name': EnemyName, 'health': 121, 'damage': 10}


def attack(person1, person2):
    person1['health'] -= person2['damage']


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

player['armor'] = 1.84
enemy['armor'] = 1.2


def attack_with_armor(person1, person2):
    person1['health'] -= int(person2['damage'] / person1['armor'])


# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
def save_user(user):
    file_name = '{}.txt'.format(user['name'])
    with open(file_name, 'w', encoding='utf-8') as file:
        for key, value in user.items():
            file.write('{}={}\n'.format(key, value))


save_user(player)
save_user(enemy)


def ludus(PlayerName, EnemyName):
    def load_user(user_name):
        file_name = user_name + '.txt'
        user = {'name': user_name}
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                key, value = line.split('=')
                if key != 'name':
                    user[key] = float(value)
        return user

    player = load_user(PlayerName)
    enemy = load_user(EnemyName)

    order = 1
    while player['health'] > 0 and enemy['health'] > 0:
        if order % 2 != 0:
            attack_with_armor(player, enemy)
        else:
            attack_with_armor(enemy, player)
        order += 1
    else:
        winner = list(filter(lambda x: x['health'] > 0, [player, enemy]))[0]
        print('Победил(а) {}! Остаток здоровья: {}'.format(winner['name'], int(winner['health'])))


ludus(PlayerName, EnemyName)
