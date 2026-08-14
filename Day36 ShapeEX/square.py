from shape import Shape


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def diagonal(self):
        return (2 * self.side ** 2) ** 0.5