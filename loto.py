#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
from random import randint

NUMBERS_MIN = 1
NUMBERS_MAX = 90
CARD_NUMBERS_COUNT = 15
CARD_LINES_COUMT = 3
CARD_WIDTH = 25
min_digits = len(str(NUMBERS_MAX)) + 1
numbers_in_line = int(CARD_NUMBERS_COUNT / CARD_LINES_COUMT)
max_digits = int(CARD_WIDTH / numbers_in_line)

class Card:
    def __init__(self):
        self.numbers = self._numbers_on_card()
        self.text = self._text_on_card()

    def _numbers_on_card(self):
        numbers_on_card = list()
        for _ in range(CARD_NUMBERS_COUNT):
            while True:
                number =  randint(NUMBERS_MIN, NUMBERS_MAX)
                if not number in numbers_on_card:
                    numbers_on_card.append(number)
                    break
        return numbers_on_card

    def _card_line(self, numbers_line):
        line = str()
        for number in numbers_line:
            while True:
                line += str(number).rjust(randint(min_digits,max_digits))
                if len(line) < CARD_WIDTH:
                    break
        return line

    def _text_on_card(self):
        numbers_on_card =  self.numbers
        text_on_card = str()
        for l in range(3):
            number_from = l*numbers_in_line
            number_to = number_from + numbers_in_line
            numbers_line = numbers_on_card[number_from:number_to]
            text_on_card += self._card_line(numbers_line)+'\n'
        return text_on_card

    def erase_number(self, number):
        text_on_card = self.text
        if ' '+str(number)+'\n' in text_on_card:
            end = '\n'
        else:
            end = ' '
        number_str = ' '+str(number)+end
        number_replace = ' '+'-'*len(str(number))+end
        self.text = text_on_card.replace(number_str, number_replace)

    def show_card(self, name):
        header_text = 'Карточка {}а'.format(name)
        print(header_text.center(CARD_WIDTH,'-'))
        print(self.text, end='')
        print('-'*CARD_WIDTH)

class Loto:
    def __init__(self):
        self._barrels = []

    def _show_barrels(self):
        if self._barrels:
            print('Номера выпавших бочонков:', self._barrels)
        else:
            pass

    def _new_barrel(self):
        while True:
            barrel = randint(NUMBERS_MIN, NUMBERS_MAX)
            if not barrel in self._barrels:
                self._barrels.append(barrel)
                return barrel
                break

    def launch_game(self):
        player_card = Card()
        computer_card = Card()
        while True:
            self._show_barrels()
            barrel = self._new_barrel()
            barrels_rest = NUMBERS_MAX+1 - NUMBERS_MIN - len(self._barrels)
            print('Новый бочонок: {} (осталось {})'.format(barrel, barrels_rest))
            player_card.show_card('игрок')
            computer_card.show_card('компьютер')
            player_choice = input('Зачеркнуть цифру? (y/n)')
            if player_choice in ('y', 'Y') and barrel in player_card.numbers:
                player_card.numbers.remove(barrel)
                print('Игрок вычеркнул номер', barrel)
                if player_card.numbers == []:
                    print('Игра окончена! Победил игрок!')
                    break
                player_card.erase_number(barrel)
            elif not(player_choice in ('y', 'Y')) and not(barrel in player_card.numbers):
                pass
            else:
                print('Игра окончена! Игрок ошибся!')
                break
            if barrel in computer_card.numbers:
               computer_card.numbers.remove(barrel)
               print('Компьютер вычеркнул номер', barrel)
               if computer_card.numbers == []:
                   print('Игра окончена! Победил компьютер!')
                   break
               computer_card.erase_number(barrel)
            next_step = input('Следующий бочонок? (y/n)')
            if barrels_rest == 0:
                print('Игра окончена! Все бочонки выпали!')
                break
            if not next_step in ('y', 'Y'):
                print('Игра прервана!')
                break
            print()

loto = Loto()
loto.launch_game()