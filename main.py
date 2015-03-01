# coding=utf-8
__author__ = 'Сероусов Виталий'

#Импортируем модуль управления интерфейсом
from Control import Control

#Создаем контейнер математических функций
container = []

#Печатаем меню
Control.menu()

#Повторение работы программы
while True:
    i = Control.try_parse("Enter command number: ")
    #Список функций
    if i == 1:
        Control.show(container)
    #Добавить новую функцию
    elif i == 2:
        Control.add(container)
    #Удалить функцию
    elif i == 3:
        Control.delete(container)
    #Сохранение данных в файл (сериализация)
    elif i == 4:
        Control.serialize(container)
    #Чтение данных из файла (десериализация)
    elif i == 5:
        res = Control.deserialize()
        if not res:
            pass
        else:
            container = res
    #Помощь
    elif i == 6:
        Control.menu()
    #Выход из программы
    elif i == 0:
        print "Application closed!"
        break
    #Повторяем, если ввели что-то не то
    else:
        continue