from abc import ABC, abstractmethod

class Movable(ABC):
    """
    Абстрактный класс, определяющий интерфейс для перемещаемых объектов.
    """
    @abstractmethod
    def move(self, commands: str):
        """
        Перемещает объект в соответствии с переданной строкой команд.
        
        commands: Строка, содержащая последовательность команд ('N', 'S', 'E', 'W').
        """
        pass

    @abstractmethod
    def path(self):
        """
        Возвращает список координат, по которым двигался объект.
        """
        pass

class Position:
    """
    Класс, представляющий координаты объекта на плоскости.
    """
    def __init__(self, x: int, y: int):
        """
        Инициализирует объект с заданными координатами, ограниченными диапазоном [0, 100].
        
        x: Начальная координата X.
        y: Начальная координата Y.
        """
        self.x = max(0, min(100, x))
        self.y = max(0, min(100, y))

    def update(self, dx: int, dy: int):
        """
        Обновляет координаты, перемещая их на заданное количество единиц.
        
        dx: Смещение по оси X.
        dy: Смещение по оси Y.
        """
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x <= 100:
            self.x = new_x
        if 0 <= new_y <= 100:
            self.y = new_y

    def __repr__(self):
        """
        Возвращает строковое представление координат.
        """
        return f'({self.x}, {self.y})'

class Robot(Movable):
    """
    Класс, представляющий робота, который может перемещаться в пределах плоскости 100x100.
    """
    def __init__(self, x: int, y: int):
        """
        Инициализирует робота с заданными начальными координатами.
        
        x: Начальная координата X.
        y: Начальная координата Y.
        """
        self.position = Position(x, y)
        self._path = [self.position]
    
    def move(self, commands: str):
        """
        Перемещает робота в соответствии с переданными командами.
        
        commands: Строка, содержащая последовательность команд ('N', 'S', 'E', 'W').
        return: Список из двух элементов [X, Y] - конечные координаты робота.
        """
        movements = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for command in commands:
            if command in movements:
                dx, dy = movements[command]
                self.position.update(dx, dy)
                self._path.append(Position(self.position.x, self.position.y))
        return [self.position.x, self.position.y]
    
    def path(self):
        """
        Возвращает список координат, по которым двигался робот.
        
        return: Список строковых представлений координат.
        """
        return [str(pos) for pos in self._path]
    
    def __call__(self, commands: str):
        """
        Позволяет вызывать объект как функцию, передавая команды для перемещения.
        
        commands: Строка, содержащая последовательность команд ('N', 'S', 'E', 'W').
        return: Список из двух элементов [X, Y] - конечные координаты робота.
        """
        return self.move(commands)


robot = Robot(50, 50)
print(robot.move("NNESW"))
print(robot.path())
print(robot("EEEESSS"))