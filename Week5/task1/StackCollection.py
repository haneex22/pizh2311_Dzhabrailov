import json
from stack import Stack

class StackCollection:
    def __init__(self, stacks=None):
        """
        Инициализация коллекции стеков
        :param stacks: начальный список стеков (по умолчанию None - пустая коллекция)
        """
        self._data = list(stacks) if stacks is not None else []

    def __str__(self):
        """Человекочитаемое представление коллекции"""
        return f"StackCollection({[str(stack) for stack in self._data]})"

    def __getitem__(self, index):
        """Доступ к элементам по индексу или срезу"""
        if isinstance(index, slice):
            return StackCollection(self._data[index])
        return self._data[index]

    def __len__(self):
        """Количество стеков в коллекции"""
        return len(self._data)

    def add(self, stack):
        """Добавляет стек в коллекцию"""
        if not isinstance(stack, Stack):
            raise TypeError("Можно добавлять только объекты класса Stack")
        self._data.append(stack)

    def remove(self, index):
        """Удаляет стек из коллекции по индексу"""
        if index < 0 or index >= len(self._data):
            raise IndexError("Индекс за пределами коллекции")
        return self._data.pop(index)

    def save(self, filename):
        """Сохраняет коллекцию в JSON-файл"""
        data = {
            "stacks": [{"items": stack.items, "max_size": stack._max_size} 
                    for stack in self._data]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename):
        """Загружает коллекцию из JSON-файла"""
        with open(filename, 'r') as f:
            data = json.load(f)
        self._data = [Stack(items=stack_data["items"], 
                        max_size=stack_data["max_size"]) 
                    for stack_data in data["stacks"]]

    @property
    def sizes(self):
        """Возвращает размеры всех стеков в коллекции"""
        return [stack.size for stack in self._data]