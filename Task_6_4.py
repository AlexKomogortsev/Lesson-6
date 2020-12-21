# Task 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('ЕДЕМ !!!')

    def stop(self):
        print('СТОООП !')

    def turn(self, direction):
        print(f'ПОВЕРНИ НА{direction.upper()}')

    def show_speed(self):
        print(f'Ваша скорость равна {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('НАРУШИТЕЛЬ ! СБАВЬ СКОРОСТЬ')
        else:
            print(f'Ваша скорость равна {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def __new__(cls, *args, **kwargs):
        pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('НАРУШИТЕЛЬ ! СБАВЬ СКОРОСТЬ')
        else:
            print(f'Ваша скорость равна {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def __new__(cls, *args, **kwargs):
        pass


police = Car(100, 'red', 'wolksvagen', is_police=True)
print(police.name)
police.go()
police.turn('лево')
police.show_speed()
police.stop()
samosval = WorkCar(60, 'черный', 'Трэк', is_police=False)
print(samosval.name)
samosval.stop()
samosval.show_speed()
camry = TownCar(60, 'белый', 'Toyota Camry', is_police=False)
print(camry.name)
camry.go()
camry.show_speed()

