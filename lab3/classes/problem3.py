from problem2 import Square


class Rectangle(Square):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        return self.length * self.width


a, b = list(map(int, input("Insert length and width of rectangle separated by space:\n").split()))
rectangle = Rectangle(a, b)
print(f'Area={rectangle.area()}')


