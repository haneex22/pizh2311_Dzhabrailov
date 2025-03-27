# Программирование на языке высокого уровня (Python).
# Задание № 2, неделя 4. Вариант 7
#
# Выполнил: Джабраилов Б.М.
# Группа: ПИЖ-б-о-23-1

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


