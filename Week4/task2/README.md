# Лабораторная работа на неделю 4, задание 2
## **Тема**: Объектно-ориентированное программирование на Python 
### Студента группы ПИЖ-б-о-23-1(1) Джабраилова Бекхана Магомедовича <br><br>
**Репозиторий Git:** https://github.com/haneex22/pizh2311_Dzhabrailov  
**Вариант: 7**  
**Практическая работа:**  
*Задание:*  
4.3.4. Stack - Стек
Прежде чем перейти к написанию кода:  
· изучите предметную область объекта и доступные операции;  
· для каждого поля и метода продумайте его область видимости, а также необходимость использования свойств.  
При реализации класс должен содержать:  
· специальные методы:  

1) __ init __(self, ... ) - инициализация с необходимыми параметрами;  
2) __ str __(self) - представление объекта в удобном для человека виде;  
3) специальные методы для возможности сложения, разности и прочих операций, которые класс должен поддерживать;

*Ответ:* 

*stack.py*
```python
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
```  
*main.py*
```python
from stack import Stack

if __name__ == "__main__":
    
    print("Тестирование класса Stack")
    print("=" * 50)
    
    # Создание стека
    s1 = Stack([1, 2, 3], max_size=5)
    print(f"Создан стек s1: {s1}")
    
    # Добавление элемента
    s1.push(4)
    print(f"После push(4): {s1}")
    
    # Просмотр верхнего элемента
    print(f"Верхний элемент (peek): {s1.peek()}")
    
    # Удаление элемента
    popped = s1.pop()
    print(f"Удаленный элемент (pop): {popped}")
    print(f"После pop(): {s1}")
    
    # Проверка на пустоту
    print(f"Стек пуст? {s1.is_empty()}")
    
    # Проверка на заполненность
    print(f"Стек заполнен? {s1.is_full()}")
    
    # Создание стека из строки
    s2 = Stack.from_string("a,b,c,d|10")
    print(f"\nСоздан стек s2 из строки: {s2}")
    
    # Сохранение и загрузка
    s2.save("stack.json")
    s3 = Stack()
    s3.load("stack.json")
    print(f"Загруженный стек s3: {s3}")
    print(f"s2 == s3? {s2 == s3}")
    
    # Очистка стека
    s3.clear()
    print(f"После clear(): {s3}")
    
    # Сложение стеков
    s4 = Stack([1, 2])
    s5 = Stack([3, 4], max_size=5)
    s6 = s4 + s5
    print(f"\nСложение стеков: {s4} + {s5} = {s6}")
    
    # Проверка свойств
    print(f"Размер s6: {s6.size}")
    print(f"Элементы s6: {s6.items}")
    
    # Проверка на переполнение
    try:
        for i in range(10):
            s6.push(i)
    except OverflowError as e:
        print(f"Ошибка: {e}")
    
    # Проверка на пустоту
    empty_stack = Stack()
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"Ошибка: {e}")

```


*Вывод программы:*  
-----
Создан стек s1: Stack([1, 2, 3], max_size=5)       <br>
После push(4): Stack([1, 2, 3, 4], max_size=5)     <br>
Верхний элемент (peek): 4 <br>
Удаленный элемент (pop): 4 <br>
После pop(): Stack([1, 2, 3], max_size=5) <br>
Стек пуст? False <br>
Стек заполнен? False <br>

Создан стек s2 из строки: Stack(['a', 'b', 'c', 'd'], max_size=10)     <br>
Загруженный стек s3: Stack(['a', 'b', 'c', 'd'], max_size=10) <br>
s2 == s3? True <br>
После clear(): Stack([], max_size=10) <br>

Сложение стеков: Stack([1, 2], max_size=None) + Stack([3, 4], max_size=5) = Stack([1, 2, 3, 4], max_size=5) <br>
Размер s6: 4 <br>
Элементы s6: (1, 2, 3, 4) <br>
Ошибка: Стек переполнен <br>
Ошибка: Стек пуст <br>


**UML Диаграмма классов:**  
![UML-diagram](UML.png)


