from math import ceil


class WinDoor:

    def __init__(self, x, y):
        self.square = x * y


class Room:

    def __init__(self, x, y, z):
        self.length = x
        self.width = y
        self.height = z
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def square(self):
        return 2 * self.height * (self.width + self.length)

    def work_surface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def roll_needed(self, w, h):
        work_square = self.work_surface()
        roll_square = w * h
        return ceil(work_square / roll_square)


def program():
    print('Напишите длины сторон комнаты:')
    x = float(input('Длина: '))
    y = float(input('Ширина: '))
    z = float(input('Высота: '))
    room = Room(x, y, z)
    print('Сколько окон в этой комнате?')
    num_of_wins = int(input())
    length_of_wins = float(input('Длина окна: '))
    width_of_wins = float(input('Ширина окна: '))
    for i in range(num_of_wins):
        room.add_wd(width_of_wins, length_of_wins)
    print('Сколько дверей в этой комнате?')
    num_of_doors = int(input())
    length_of_doors = float(input('Длина двери: '))
    width_of_doors = float(input('Ширина двери: '))
    for i in range(num_of_doors):
        room.add_wd(width_of_doors, length_of_doors)
    print(f'Комната {x}x{y}x{z} метров создана. В ней: окон - {num_of_wins}, дверей - {num_of_doors}.')
    print('Напишите размеры рулона обоев, чтобы вычислить их количество, необходимое для обклейки комнаты.')
    length_of_roll = float(input('Длина: '))
    width_of_roll = float(input('Ширина: '))
    print(f'Оклеиваемая площадь комнаты составляет {room.work_surface()}. '
          f'Количество необходимых рулонов - {room.roll_needed(length_of_roll, width_of_roll)}')


program()