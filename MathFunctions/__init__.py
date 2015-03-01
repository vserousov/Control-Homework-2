# coding=utf-8
__author__ = 'Сероусов Виталий'


class OneArgument(object):
    """
    Абстрактный класс "Функция одного аргумента"
    """
    def __init__(self):
        """
        Конструктор нельзя вызвать
        Имитируем абстрактный класс
        """
        raise NotImplementedError()

    def parameters(self, *params):
        """
        Установка списка параметров
        """
        pass

    def calculate(self, x):
        """
        Вычисление значения функции при заданном аргументе x
        """
        pass

    def write(self):
        """
        Печать функции на экран
        """
        pass


class Linear(OneArgument):
    """
    Класс "Линейная функция"
    """
    def __init__(self):
        try:
            super(Linear, self).__init__(self)
        except:
            self.a = self.b = False

    def parameters(self, a, b):
        self.a, self.b = float(a), float(b)

    def calculate(self, x):
        if not self.a or not self.b:
            raise Exception("Coefficients are not set")
        return self.a * x + self.b

    def write(self):
        return "f(x) = " + str(self.a) + "x + " + str(self.b)


class Hyperbola(OneArgument):
    """
    Класс "Гипербола"
    """
    def __init__(self):
        try:
            super(Hyperbola, self).__init__(self)
        except:
            self.a = False

    def parameters(self, a):
        self.a = float(a)

    def calculate(self, x):
        if x == 0:
            raise ZeroDivisionError
        if not self.a:
            raise Exception("Coefficients are not set")
        return self.a / x

    def write(self):
        return "f(x) = " + str(self.a) + "/x"


class Parabola(OneArgument):
    """
    Класс "Парабола"
    """
    def __init__(self):
        try:
            super(Parabola, self).__init__(self)
        except:
            self.a = self.b = self.c = False

    def parameters(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)

    def calculate(self, x):
        if not self.a or not self.b or not self.c:
            raise Exception("Coefficients are not set")
        return self.a * (x ** 2) + self.b * x + self.c

    def write(self):
        return "f(x) = " + str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c)
