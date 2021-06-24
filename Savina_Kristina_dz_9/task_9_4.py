class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} едет!'.format(self.name))

    def stop(self):
        print('{} остановитесь!'.format(self.name))

    def turn(self, direction):
        print('{} возьмите {}!'.format(self.name, direction))

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Ваша скорость привышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Внимание! Ваша скорость привышена!')


class PoliceCar(Car):
    pass


sport_car = SportCar(180, 'Красная', 'Спортивная машина', False)
town_car = TownCar(90, 'Синяя', 'Городская машина', False)
work_car = WorkCar(60, 'Оранжевая', 'Рабочая машина', False)
police_car = PoliceCar(200, 'Черная', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('левее')
