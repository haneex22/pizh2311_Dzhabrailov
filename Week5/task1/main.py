from stack import Stack
from StackCollection import StackCollection

if __name__ == "__main__":

    # Создание стеков
    s1 = Stack([1, 2, 3], max_size=5)
    s2 = Stack([4, 5, 6], max_size=10)
    s3 = Stack(["a", "b", "c"])
    
    # Создание коллекции
    collection = StackCollection([s1, s2])
    print(f"Создана коллекция: {collection}")
    
    # Добавление стека
    collection.add(s3)
    print(f"После добавления стека: {collection}")
    
    # Доступ по индексу
    print(f"Первый стек в коллекции: {collection[0]}")
    
    # Срез
    print(f"Срез коллекции: {collection[1:]}")
    
    # Удаление стека
    removed = collection.remove(1)
    print(f"Удален стек: {removed}")
    print(f"Коллекция после удаления: {collection}")
    
    # Сохранение и загрузка
    collection.save("stacks.json")
    new_collection = StackCollection()
    new_collection.load("stacks.json")
    print(f"Загруженная коллекция: {new_collection}")
    
    # Свойство sizes
    print(f"Размеры стеков в коллекции: {new_collection.sizes}")

