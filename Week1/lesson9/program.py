import room


def program():
    print('Напишите длины сторон комнаты:')
    x = float(input('Длина: '))
    y = float(input('Ширина: '))
    z = float(input('Высота: '))
    room_1 = room.Room(x, y, z)
    print('Сколько окон в этой комнате?')
    num_of_wins = int(input())
    length_of_wins = float(input('Длина окна: '))
    width_of_wins = float(input('Ширина окна: '))
    for i in range(num_of_wins):
        room_1.add_wd(width_of_wins, length_of_wins)
    print('Сколько дверей в этой комнате?')
    num_of_doors = int(input())
    length_of_doors = float(input('Длина двери: '))
    width_of_doors = float(input('Ширина двери: '))
    for i in range(num_of_doors):
        room_1.add_wd(width_of_doors, length_of_doors)
    print(f'Комната {x}x{y}x{z} метров создана. В ней: окон - {num_of_wins}, дверей - {num_of_doors}.')
    print('Напишите размеры рулона обоев, чтобы вычислить их количество, необходимое для обклейки комнаты.')
    length_of_roll = float(input('Длина: '))
    width_of_roll = float(input('Ширина: '))
    print(f'Оклеиваемая площадь комнаты составляет {room_1.work_surface()}. '
          f'Количество необходимых рулонов - {room_1.roll_needed(length_of_roll, width_of_roll)}')


program()
