import math

class Figure:
    sides_count = 0
    def __init__(self, color: list[int, int, int], *sides, filled = False):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        d = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        t = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return d and t
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b
    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if isinstance(i, int) and len(self.__sides) == len(new_sides) and i >=0:
                return True
            else:
                return False
    def get_sides(self):
        return self.__sides[0]
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color: list [int, int, int], lenght, filled=False):
        super().__init__(color, lenght, filled=filled)
        self.__radius = lenght / (2 * math.pi)

    def get_square(self):
        return list(len(self)**2 // (4 * math.pi))

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: tuple [int, int, int], height, *sides, filled=False):
        super().__init__(color, sides, filled=filled)
        self.height = height
    def get_square(self):
        p = len(self)/2
        sides = self.get_sides()
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    sides_count = 12
    def __init__(self, color: list [int, int, int],side, filled=False):
        cube_side = [side] * 12
        super().__init__(color, cube_side, filled=filled)
        #self.__sides = list(sides) * 12
    def get_volume(self):
        return self.get_sides()[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())