import time


class TrafficLight:
    def __init__(self):
        self.__color1 = 'red'
        self.__color2 = 'yellow'
        self.__color3 = 'green'

    def running(self):
        print(self.__color1)
        time.sleep(7)
        print(self.__color2)
        time.sleep(2)
        print(self.__color3)


if __name__ == '__main__':
    a = TrafficLight()
    a.running()
