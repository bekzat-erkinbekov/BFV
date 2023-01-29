class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def calculate_area(self):
        return 3.14 * (self.__radius ** 2)

    def info(self):
        return (f'{self.calculate_area()} {self.unit} {self.__radius} {self.unit}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.side_a = value

    @property
    def side_b(self):
        return self.__side_b

    @side_b.setter
    def side_b(self, value):
        self.__side_b = value


    def calculate_area(self):
        return round(1 / 2 * (self.__side_a * self.__side_b), 2)

    def info(self):
        return f"side_a : {self.__side_a}{self.unit}, side_b : {self.__side_b}{self.unit}2, " \
               f"area: {self.calculate_area()}{self.unit}"
circle = Circle(4)
print(circle.info())
triangel = RightTriangle(99,88)
print(triangel.info())
print()
