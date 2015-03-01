# coding=utf-8
__author__ = 'Сероусов Виталий'

from MathFunctions import *
import pickle


class Control(object):
    """
    Cтатический класс
    для управления интерфейсом программы
    """

    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def try_parse(text):
        """
        Парсинг int и float
        :param text: Сообщение
        :return: Число типа int или float
        """
        val = raw_input(text)
        try:
            if '.' in val:
                return float(val)
            else:
                return int(val)
        except:
            return Control.try_parse(text)

    @staticmethod
    def menu():
        """
        Список комманд
        """
        print "Inteface of console application:"
        print "1) Show the list of math functions"
        print "2) Add new function"
        print "3) Delete function"
        print "4) Save data in file"
        print "5) Load data from file"
        print "6) Help"
        print "To exit enter 0"

    @staticmethod
    def show(container):
        """
        Вывод списка функций при заданном пользователем значении аргумента
        :param container: контейнер данных
        """
        if len(container) == 0:
            print "There are no functions."
            return
        x = Control.try_parse("Enter function argument x to calculate value: ")
        print "The list of functions sorted by value in format (Number | Value | View):"
        try:
            container.sort(key=lambda y: y.calculate(x))
        except ZeroDivisionError as ex:
            print "Some function are hyperbolic, that's why the value doesn't exist at x = 0"
        k = 0
        for f in container:
            try:
                print str(k) + " | f(" + str(x) + ") = " + str(f.calculate(x)) + " | " + f.write()
            except:
                print str(k) + " | Doesn't exist | " + f.write()
            k += 1

    @staticmethod
    def add(container):
        """
        Добавление функции в контейнер
        :param container: Контейнер данных
        """
        print "Type of function:"
        print "1) Linear"
        print "2) Hyperbola"
        print "3) Parabola"
        num = Control.try_parse("Enter the number of function type: ")
        # Линейная функция
        if num == 1:
            a = Control.try_parse("Enter the linear coefficient: ")
            b = Control.try_parse("Enter the constant: ")
            func = Linear()
            func.parameters(a, b)
            container.append(func)
        #Гиперболическая функция
        if num == 2:
            a = Control.try_parse("Enter the coefficient of 1/x: ")
            func = Hyperbola()
            func.parameters(a)
            container.append(func)
        #Параболическая функция
        if num == 3:
            a = Control.try_parse("Enter the quadratic coefficient: ")
            b = Control.try_parse("Enter the linear coefficient: ")
            c = Control.try_parse("Enter the constant: ")
            func = Parabola()
            func.parameters(a, b, c)
            container.append(func)

    @staticmethod
    def delete(container):
        """
        Удаление функции из контейнера
        :param container: Контейнер данных
        """
        try:
            del container[Control.try_parse("Enter the number of function you want to remove: ")]
            print "Successfully removed!"
        except:
            print "Error! The function with this number doesn't exist in database."

    @staticmethod
    def serialize(container):
        """
        Сериализация данных в файл
        :param container: Контейнер данных
        """
        with open('data.txt', 'wb') as f:
            pickle.dump(container, f)
            print "Information saved in file data.txt"

    @staticmethod
    def deserialize():
        """
        Десериализация данных из файла
        :return: Данные
        """
        try:
            with open('data.txt', 'rb') as f:
                print "Information loaded from file data.txt"
                return pickle.load(f)
        except IOError as e:
            print "Error! There is no file data.txt."
            return False
        except:
            print "Error! Can't read file."
            return False