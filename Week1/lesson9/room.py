"""Модуль содержит классы комнат, окон и дверей."""

"""Импортируем метод округления числа вверх"""
from math import ceil


"""Класс, отвечающий за создание окон и дверей в комнате"""


class WinDoor:

    """Конструктор класса. Возвращает площадь окна или двери"""
    def __init__(self, x, y):
        self.square = x * y


"""Класс, отвечающий за создание комнаты"""


class Room:

    """Конструктор класса.
    Создает комнату размерами x*y*z и пустой список wd, в который будут записываться площади окон и дверей"""
    def __init__(self, x, y, z):
        self.length = x
        self.width = y
        self.height = z
        self.wd = []

    """Метод, добавляющий окно или дверь в список wd"""
    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    """Метод подсчета площади оклеиваемых стен комнаты"""
    def square(self):
        return 2 * self.height * (self.width + self.length)

    """Метод подсчета площади оклеиваемых стен комнаты с учетом окон и дверей"""
    def work_surface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    """Метод подсчета количества необходимых рулонов обоев для оклеивания комнаты"""
    def roll_needed(self, w, h):
        work_square = self.work_surface()
        roll_square = w * h
        return ceil(work_square / roll_square)
