# Программирование на языке высокого уровня (Python).
# Задание № 2, неделя 4. Вариант 7
#
# Выполнил: Джабраилов Б.М.
# Группа: ПИЖ-б-о-23-1

import json

class Stack:
    def __init__(self, items=None, max_size=None):
        """
        Инициализация стека
        items: начальные элементы стека (по умолчанию None - пустой стек)
        max_size: максимальный размер стека (по умолчанию None - без ограничений)
        """
        self._items = list(items) if items is not None else []
        self._max_size = max_size

    def __str__(self):
        """Представление стека в виде строки"""
        return f"Stack({self._items}, max_size={self._max_size})"

    def __len__(self):
        """Возвращает количество элементов в стеке"""
        return len(self._items)

    def __add__(self, other):
        """Объединение двух стеков"""
        if not isinstance(other, Stack):
            raise TypeError("Можно объединять только с другим стеком")
        
        new_max_size = None
        if self._max_size is not None and other._max_size is not None:
            new_max_size = self._max_size + other._max_size
        elif self._max_size is not None:
            new_max_size = self._max_size
        elif other._max_size is not None:
            new_max_size = other._max_size
            
        return Stack(self._items + other._items, new_max_size)

    def __eq__(self, other):
        """Проверка на равенство двух стеков"""
        if not isinstance(other, Stack):
            return False
        return self._items == other._items and self._max_size == other._max_size

    @classmethod
    def from_string(cls, str_value):
        """
        Создает стек из строки
        Формат строки: "элемент1,элемент2,...|максимальный_размер"
        """
        if "|" in str_value:
            items_part, max_size_part = str_value.split("|")
            max_size = int(max_size_part) if max_size_part else None
        else:
            items_part = str_value
            max_size = None

        items = [item.strip() for item in items_part.split(",")] if items_part else []
        return cls(items, max_size)

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        if self.is_full():
            raise OverflowError("Стек переполнен")
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()

    def peek(self):
        """Возвращает элемент с вершины стека без его удаления"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self._items) == 0

    def is_full(self):
        """Проверяет, заполнен ли стек"""
        return self._max_size is not None and len(self._items) >= self._max_size

    def clear(self):
        """Очищает стек"""
        self._items = []

    def save(self, filename):
        """Сохраняет стек в JSON-файл"""
        data = {
            "items": self._items,
            "max_size": self._max_size
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename):
        """Загружает стек из JSON-файла"""
        with open(filename, 'r') as f:
            data = json.load(f)
        self._items = data["items"]
        self._max_size = data["max_size"]

    @property
    def size(self):
        """Возвращает текущий размер стека"""
        return len(self._items)

    @property
    def items(self):
        """Возвращает элементы стека (только для чтения)"""
        return tuple(self._items)
