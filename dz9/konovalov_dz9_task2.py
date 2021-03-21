class Road:
    def __init__(self, _length, _width):
        self._length = length
        self._width = width

    def result_v(self):
        depth = 5
        weight = 25
        return self._width * self._length * depth * weight


if __name__ == '__main__':
    length = int(input("Enter to length: "))
    width = int(input("Enter to width: "))
    calc = Road(length, width)
    print(calc.result_v())





