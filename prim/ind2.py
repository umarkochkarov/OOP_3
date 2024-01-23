from abc import ABC, abstractmethod

class Root(ABC):
    @abstractmethod
    def calculate_roots(self):
        pass

    @abstractmethod
    def display_result(self):
        pass


def display(root_object):
    print(f"Результат: {root_object}")


class Linear(Root):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.roots = self.calculate_roots()

    def calculate_roots(self):
        if self.a == 0:
            if self.b == 0:
                return "Бесконечное количество корней"
            else:
                return "Нет корней"
        else:
            root = -self.b / self.a
            return [root]

    def display_result(self):
        print("Линейное уравнение:")
        print(f"{self.a}x + {self.b} = 0")
        print("Корни:", self.roots)

    def __str__(self):
        return f"Линейное уравнение: {self.a}x + {self.b} = 0"


class Square(Root):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = self.calculate_roots()

    def calculate_roots(self):
        delta = self.b ** 2 - 4 * self.a * self.c

        if delta > 0:
            root1 = (-self.b + (delta ** 0.5)) / (2 * self.a)
            root2 = (-self.b - (delta ** 0.5)) / (2 * self.a)
            return [root1, root2]
        elif delta == 0:
            root = -self.b / (2 * self.a)
            return [root]
        else:
            return "Нет действительных корней"

    def display_result(self):
        print("Квадратное уравнение:")
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")
        print("Корни:", self.roots)

    def __str__(self):
        return f"Квадратное уравнение: {self.a}x^2 + {self.b}x + {self.c} = 0"


if __name__ == '__main__':
    linear_equation = Linear(2, -3)
    linear_equation.display_result()
    display(linear_equation)

    square_equation = Square(1, -3, 2)
    square_equation.display_result()
    display(square_equation)
