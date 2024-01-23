import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def set_sides(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_angles(self):
        angle1 = math.degrees(math.acos((self.side2 ** 2 + self.side3 ** 2 - self.side1 ** 2) / (2 * self.side2 * self.side3)))
        angle2 = math.degrees(math.acos((self.side1 ** 2 + self.side3 ** 2 - self.side2 ** 2) / (2 * self.side1 * self.side3)))
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Equilateral(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.area = self.calculate_area()

    def calculate_area(self):
        # Формула площади равностороннего треугольника
        return (math.sqrt(3) / 4) * self.side1 ** 2


# Пример использования с вводом значений от пользователя:
side1 = float(input("Введите длину первой стороны треугольника: "))
side2 = float(input("Введите длину второй стороны треугольника: "))
side3 = float(input("Введите длину третьей стороны треугольника: "))

triangle = Triangle(side1, side2, side3)
print("Периметр треугольника:", triangle.calculate_perimeter())
print("Углы треугольника:", triangle.calculate_angles())

side_equilateral = float(input("Введите длину стороны равностороннего треугольника: "))
equilateral_triangle = Equilateral(side_equilateral)
print("Периметр равностороннего треугольника:", equilateral_triangle.calculate_perimeter())
print("Площадь равностороннего треугольника:", equilateral_triangle.area)
