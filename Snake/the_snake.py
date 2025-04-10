"""
Модуль для игры 'Змейка' (Изгиб Питона).

Реализация классической игры 'Змейка' с использованием PyGame и ООП.
"""

import pygame
import random

# Константы для размеров поля и сетки
SCREEN_WIDTH = 640    # Ширина игрового поля в пикселях
SCREEN_HEIGHT = 480   # Высота игрового поля в пикселях
GRID_SIZE = 20        # Размер одной ячейки сетки
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE   # Ширина в ячейках
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE # Высота в ячейках

# Направления движения змейки
UP = (0, -1)    # Движение вверх
DOWN = (0, 1)   # Движение вниз
LEFT = (-1, 0)  # Движение влево
RIGHT = (1, 0)  # Движение вправо

# Цвета
BOARD_BACKGROUND_COLOR = (0, 0, 0)      # Черный цвет фона
BORDER_COLOR = (93, 216, 228)          # Цвет границ ячеек
APPLE_COLOR = (255, 0, 0)              # Красный цвет яблока
SNAKE_COLOR = (0, 255, 0)              # Зеленый цвет змейки

# Скорость движения змейки (кадров в секунду)
SPEED = 20

# Настройка игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')  # Заголовок окна
clock = pygame.time.Clock()           # Для контроля скорости игры


class GameObject:
    """
    Базовый класс для всех игровых объектов.
    
    Содержит общие атрибуты и методы для игровых объектов.
    """
    
    def __init__(self, position=None, body_color=None):
        """
        Инициализация игрового объекта.
        
        Args:
            position (tuple): Начальная позиция объекта (x, y). По умолчанию - центр экрана.
            body_color (tuple): Цвет объекта в формате RGB.
        """
        self.position = position if position else (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color
    
    def draw(self):
        """Абстрактный метод для отрисовки объекта (должен быть переопределен в дочерних классах)."""
        pass


class Apple(GameObject):
    """
    Класс для представления яблока в игре.
    
    Наследуется от GameObject.
    """
    
    def __init__(self):
        """
        Инициализация яблока.
        
        Устанавливает красный цвет и случайную начальную позицию.
        """
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position()
    
    def randomize_position(self, snake_positions=None):
        """
        Устанавливает случайную позицию для яблока.
        
        Args:
            snake_positions (list): Список позиций, занятых змейкой.
                                   Если None, считается пустым списком.
        """
        if snake_positions is None:
            snake_positions = []
        
        # Генерация позиции, не занятой змейкой
        while True:
            x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
            y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            if (x, y) not in snake_positions:
                self.position = (x, y)
                break
    
    def draw(self):
        """
        Отрисовывает яблоко на игровом поле.
        
        Рисует квадрат с границей по текущим координатам.
        """
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    Класс для представления змейки в игре.
    
    Наследуется от GameObject.
    """
    
    def __init__(self):
        """
        Инициализация змейки.
        
        Устанавливает зеленый цвет, начальную позицию и направление движения.
        """
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()
    
    def reset(self):
        """Сбрасывает змейку в начальное состояние (длина 1, движение вправо)."""
        self.positions = [self.position]  # Список позиций сегментов
        self.length = 1                  # Текущая длина змейки
        self.direction = RIGHT           # Текущее направление движения
        self.next_direction = None       # Следующее направление (после обработки клавиш)
        self.last = None                 # Позиция последнего удаленного сегмента
    
    def update_direction(self):
        """Обновляет направление движения на основе нажатых клавиш."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None
    
    def get_head_position(self):
        """
        Возвращает позицию головы змейки.
        
        Returns:
            tuple: Координаты (x, y) головы змейки.
        """
        return self.positions[0]
    
    def move(self):
        """Перемещает змейку на одну ячейку в текущем направлении."""
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        
        # Расчет новой позиции головы с учетом прохождения через границы
        new_x = (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT
        
        # Сохраняем последний сегмент для затирания
        self.last = self.positions[-1] if len(self.positions) > 1 else None
        
        # Добавляем новую голову
        self.positions.insert(0, (new_x, new_y))
        
        # Удаляем хвост, если змейка не выросла
        if len(self.positions) > self.length:
            self.positions.pop()
    
    def draw(self):
        """
        Отрисовывает змейку на игровом поле.
        
        Рисует все сегменты змейки и затирает последний удаленный сегмент.
        """
        # Отрисовка тела змейки (кроме головы)
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        
        # Отрисовка головы змейки
        if self.positions:
            head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, head_rect)
            pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)
        
        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)


def handle_keys(game_object):
    """
    Обрабатывает нажатия клавиш для управления змейкой.
    
    Args:
        game_object (Snake): Объект змейки, которым управляет игрок.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Основная функция игры, содержащая главный игровой цикл."""
    pygame.init()
    
    # Создание объектов игры
    snake = Snake()
    apple = Apple()
    record = 1  # Рекордная длина змейки
    
    while True:
        clock.tick(SPEED)  # Контроль скорости игры
        
        # Обработка ввода
        handle_keys(snake)
        snake.update_direction()
        
        # Движение змейки
        snake.move()
        
        # Проверка съедания яблока
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)
            if snake.length > record:
                record = snake.length
                pygame.display.set_caption(f'Змейка (Рекорд: {record})')
        
        # Проверка столкновения с собой
        if snake.length > 3 and snake.get_head_position() in snake.positions[1:]:
            snake.reset()
        
        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()