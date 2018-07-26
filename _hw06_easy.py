# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, name, color):
        self.speed = 0
        self.name = name
        self.color = color
        self._is_police = False

    def go(self, speed):
        max_town_speed = 180
        if speed <= max_town_speed:
            self.speed = speed
        else:
            self.speed = max_town_speed
        print('Машина ({}, {}) поехала со скоростью {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина ({}, {}) остановилась'.format(self.name, self.color))

    def turn(self, direction):
        print('Машина ({}, {}) повернула {}'.format(self.name, self.color, direction))

    def set_is_police(self):
        self._is_police = True

    def police_siren_reaction(self):
        if self._is_police:
            print('({}, {}) на связи'.format(self.name, self.color))
        else:
            self.stop()


red_mazda = TownCar('Mazda CX-9', 'красный')
red_mazda.go(70)
red_mazda.set_is_police()
red_mazda.police_siren_reaction()


class SportCar:
    def __init__(self, name, color):
        self.speed = 0
        self.name = name
        self.color = color
        self._is_police = False

    def go(self, speed):
        self.speed = speed
        print('Машина ({}, {}) поехала со скоростью {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина ({}, {}) остановилась'.format(self.name, self.color))

    def turn(self, direction=''):
        critical_speed = 200
        if self.speed < critical_speed:
            print('Машина ({}, {}) повернула {}'.format(self.name, self.color, direction))
        else:
            print('Авария!')
            self.stop()

    def police_siren_reaction(self):
        self.go(self.speed * 2)


orange_sport_cayenne = SportCar('Porsche Cayenne', 'оранжевый')
orange_sport_cayenne.go(90)
orange_sport_cayenne.police_siren_reaction()
orange_sport_cayenne.speed += 20
orange_sport_cayenne.turn()


class WorkCar:
    def __init__(self, name):
        self.speed = 0
        self.name = name
        self.color = 'жёлтый'
        self.is_police = False

    def go(self, speed):
        max_belaz_speed = 90
        if speed <= max_belaz_speed:
            self.speed = speed
        else:
            self.speed = max_belaz_speed
        print('Машина ({}, {}) поехала со скоростью {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина ({}, {}) остановилась'.format(self.name, self.color))

    def turn(self, direction):
        print('Машина ({}, {}) повернула {}'.format(self.name, self.color, direction))

    def police_siren_reaction(self):
        print('Машина ({}, {}) с сопровождением'.format(self.name, self.color))


belaz = WorkCar('белАЗ-75710')
belaz.go(100)
belaz.stop()
belaz.police_siren_reaction()
belaz.turn('в сторону шахты')


class PoliceCar:
    def __init__(self, name):
        self.speed = 0
        self.name = name
        self.color = "синий"
        self.is_police = True

    def go(self, speed):
        max_logan_speed = 180
        if speed <= max_logan_speed:
            self.speed = speed
        else:
            self.speed = max_logan_speed
        print('Машина ({}, {}) поехала со скоростью {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина ({}, {}) остановилась'.format(self.name, self.color))

    def turn(self, direction):
        print('Машина ({}, {}) повернула {}'.format(self.name, self.color, direction))

    def police_siren_reaction(self):
        print('({}, {}) на связи'.format(self.name, self.color))


police_logan = PoliceCar('Renault Logan')
police_logan.go(90)
police_logan.police_siren_reaction()


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name, max_speed, color):
        self.speed = 0
        self.name = name
        self.max_speed = max_speed
        self.color = color

    def go(self, speed):
        if speed <= self.max_speed:
            self.speed = speed
        else:
            self.speed = self.max_speed
        print('Машина ({}, {}) поехала со скоростью {} км/ч'.format(self.name, self.color, self.speed))

    def stop(self):
        self.speed = 0
        print('Машина ({}, {}) остановилась'.format(self.name, self.color))

    def turn(self, direction=''):
        if self.speed < self.max_speed:
            print('Машина ({}, {}) повернула {}'.format(self.name, self.color, direction))
        else:
            print('Авария!')
            self.stop()


class TownCar(Car):
    def __init__(self, name, max_speed, color):
        super().__init__(name, max_speed, color)
        self._is_police = False

    def set_is_police(self):
        self._is_police = True

    def police_siren(self):
        if self._is_police:
            print('({}, {}) на связи'.format(self.name, self.color))
        else:
            self.stop()


print()
red_mazda = TownCar('Mazda CX-9', 180, 'красный')
red_mazda.go(70)
red_mazda.set_is_police()
red_mazda.police_siren()


class SportCar(Car):
    def __init__(self, color, name, max_speed):
        super().__init__(color, name, max_speed)
        self.is_police = False

    def police_siren_reaction(self):
        self.go(self.speed * 2)


orange_sport_cayenne = SportCar('Porsche Cayenne', 200, 'оранжевый')
orange_sport_cayenne.go(90)
orange_sport_cayenne.police_siren_reaction()
orange_sport_cayenne.speed += 20
orange_sport_cayenne.turn()


class WorkCar(Car):
    def __init__(self, name, max_speed, color='жёлтый'):
        super().__init__(name, max_speed, color)
        self.is_police = False

    def police_siren_reaction(self):
        print('Машина ({}, {}) с сопровождением'.format(self.name, self.color))


belaz = WorkCar('белАЗ-75710', 90)
belaz.go(100)
belaz.stop()
belaz.police_siren_reaction()
belaz.turn('в сторону шахты')


class PoliceCar(Car):
    def __init__(self, name, max_speed, color='синий'):
        super().__init__(name, max_speed, color)
        self.is_police = True

    def police_siren_reaction(self):
        print('({}, {}) на связи'.format(self.name, self.color))


police_logan = PoliceCar('Renault Logan', 180)
police_logan.go(90)
police_logan.police_siren_reaction()