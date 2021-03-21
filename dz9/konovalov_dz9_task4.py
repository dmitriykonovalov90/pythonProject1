class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        if is_police is True:
            print("This is a police car!")

    def go(self):
        print(self.name, 'go-go')

    def stop(self):
        print(self.name, 'stop\n')

    def turn(self, direction):
        print(self.name, 'turn', direction)

    def show_speed(self):
        print('current speed = ', self.speed)


class TownCar(Car):
    def town_car(self):
        self.name = 'Honda fit'
        self.color = 'red'
        self.is_police = False
        return f'car: {self.name} \ncolor: {self.color}\nspeed: {self.speed}'

    def show_speed(self):
        if self.speed > 60:
            print('Over speed!!!! Max = 60, your speed = ', self.speed)


class SportCar(Car):
    def sport_car(self):
        self.name = 'Honda accord'
        self.color = 'white'
        self.is_police = False
        return f'car: {self.name} \ncolor: {self.color}\nspeed: {self.speed}'


class WorkCar(Car):
    def work_car(self):
        self.name = 'Honda freed'
        self.color = 'blue'
        self.is_police = False
        return f'car: {self.name} \ncolor: {self.color}\nspeed: {self.speed}'

    def show_speed(self):
        if self.speed > 40:
            print('Over speed!!!! Max = 40, your speed = ', self.speed)


class PoliceCar(Car):
    def police_car(self):
        self.name = 'Honda civic'
        self.color = 'white'
        return f'car: {self.name} \ncolor: {self.color}\nspeed: {self.speed}'


if __name__ == '__main__':
    execute_work = WorkCar(100, '1', 'name', False)
    print(execute_work.work_car())
    execute_work.go()
    execute_work.turn('left')
    execute_work.show_speed()
    execute_work.stop()

    execute_police = PoliceCar(100, '1', 'name', False)
    print(execute_police.police_car())
    execute_police.go()
    execute_police.turn('left')
    execute_police.show_speed()
    execute_police.stop()

    execute_town = TownCar(100, '1', 'name', False)
    print(execute_town.town_car())
    execute_town.go()
    execute_town.turn('left')
    execute_town.show_speed()
    execute_town.stop()

    execute_sport = SportCar(100, '1', 'name', False)
    print(execute_sport.sport_car())
    execute_sport.go()
    execute_sport.turn('right')
    execute_sport.show_speed()
    execute_sport.stop()
