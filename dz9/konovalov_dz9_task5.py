class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('starting drawing')


class Pen(Stationery):
    def draw(self):
        print(f'starting drawing with a {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'starting drawing with a {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'starting drawing with a {self.title}')


if __name__ == '__main__':
    base_draw = Stationery('base class')
    base_draw.draw()

    pen = Pen('pen')
    pen.draw()

    pencil = Pencil('pencil')
    pencil.draw()

    handle = Handle('handle')
    handle.draw()
