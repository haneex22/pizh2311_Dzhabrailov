# Программирование на языке высокого уровня (Python).
# Задание № 2, неделя 3. Вариант 8
#
# Выполнил: Джабраилов Б.М.
# Группа: ПИЖ-б-о-23-1



import time


class Заказ:
    """Класс Заказ содержит информацию о заказе."""

    # Переменная класса для определения номера заказа
    счетчик_заказов = 0

    def __init__(self):
        """Конструктор класса."""
        # Хранит экземпляры класса Пицца и его потомков
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1
        self.номер_заказа = Заказ.счетчик_заказов

    def __str__(self):
        """Вернуть содержимое заказа и его сумму.

        Формат вывода:

        Заказ №2
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        Сумма заказа: 800.00 р.

        """
        res = f"Заказ №{self.номер_заказа}\n"
        for i, пицца in enumerate(self.заказанные_пиццы, 1):
            res += f"{i}. {пицца}\n"
        res += f"Сумма заказа: {self.сумма():.2f} р.\n"
        return res

    def добавить(self, пицца):
        """Добавить пиццу в заказ."""
        self.заказанные_пиццы.append(пицца)
        print(f"Пицца {пицца.название} добавлена!")

    def сумма(self):
        """Вернуть сумму заказа."""
        return sum(пицца.цена for пицца in self.заказанные_пиццы)

    def выполнить(self):
        """Выполнить заказ.

        Для каждой пиццы в заказе: подготовить, испечь, нарезать и упаковать.
        Сообщить, что заказ готов и пожелать приятного аппетита.

        Для визуального эффекта, каждое действие осуществляется с "задержкой",
        используя time.sleep(1).

        Формат вывода:

        Заказ поступил на выполнение...
        1. Пепперони
        Начинаю готовить пиццу Пепперони
          - замешиваю тонкое тесто...
          - добавляю соус: томатный...
          - и, конечно: пепперони, сыр моцарелла...
        Выпекаю пиццу... Готово!
        Нарезаю на аппетитные кусочки...
        Упаковываю в фирменную упаковку и готово!

        Заказ №2 готов! Приятного аппетита!
        """
        print("Заказ поступил на выполнение...")
        for пицца in self.заказанные_пиццы:
            print(f"{пицца.название}")
            пицца.подготовить()
            time.sleep(1)
            пицца.испечь()
            time.sleep(1)
            пицца.нарезать()
            time.sleep(1)
            пицца.упаковать()
            time.sleep(1)
            print()
        print(f"Заказ №{self.номер_заказа} готов! Приятного аппетита!")