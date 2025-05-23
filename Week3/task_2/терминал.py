# Программирование на языке высокого уровня (Python).
# Задание № 2, неделя 3. Вариант 8
#
# Выполнил: Джабраилов Б.М.
# Группа: ПИЖ-б-о-23-1


from пицца import ПиццаПепперони, ПиццаБарбекю, ПиццаДарыМоря
from заказ import Заказ


class Терминал:
    """Класс Терминал обеспечивает взаимодействие с клиентом."""

    КОМПАНИЯ = "Пиццерия #1"
    КОМАНДА_ОТМЕНА_ЗАКАЗА = -1
    КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА = 0

    def __init__(self):
        """Конструктор класса.

        self.меню: список доступных пицц;
        self.заказ: список заказанных пицц;
        self.отображать_меню: определяет отображение меню
                              равен True: при создании терминала,
                              после отмены или подтверждения заказа.
        """
        # Доступные пиццы
        self.меню = [ПиццаПепперони(), ПиццаБарбекю(), ПиццаДарыМоря()]
        self.заказ = None
        self.отображать_меню = True

    def __str__(self):
        """Вернуть строковое представление класса.

        Формат вывода:

        Имя пиццерии, версия программы.
        """
        return f"{Терминал.КОМПАНИЯ}, версия 1.0"

    def показать_меню(self):
        """Показать меню.

        Показать меню следует только при наличии флага self.отображать_меню
        self.отображать_меню устанавливается в False после вывода меню.

        Формат вывода:

        Пиццерия #1
        Добро пожаловать!

        Меню:
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        3. Пицца: Дары моря | Цена: 550.00 р.
           Тесто: пышное Соус: тар-тар
           Начинка: кальмары, креветки, мидии, сыр моцарелла
        Для выбора укажите цифру через <ENTER>.
        Для отмены заказа введите -1
        Для подтверждения заказа введите 0
        """
        if not self.отображать_меню:
            return

        print(f"{Терминал.КОМПАНИЯ}")
        print("Добро пожаловать!\n")
        print("Меню:")
        for i, пицца in enumerate(self.меню, 1):
            print(f"{i}. {пицца}")
        print("Для выбора укажите цифру через <ENTER>.")
        print("Для отмены заказа введите -1")
        print("Для подтверждения заказа введите 0\n")

        self.отображать_меню = False

    def обработать_команду(self, пункт_меню):
        """Обработать действие пользователя.

        Аргументы:
          - пункт_меню (str): выбор пользователя.

        Возможные значения "пункт_меню":
          - -1: отменить заказ;
          -  0: подтвердить заказ; при этом осуществляется
                выставление счета, оплата, а также выполняется заказ;
                после заказ удаляется (= None)
          - 1..len(self.меню): добавление пиццы к добавить_к_заказу;
                               если заказ не создан, его нужно создать.
          - иначе: сообщить о невозможности обработать команду.

        Каждое действие подтверждается выводом на экран, например:
        1
        Пицца Пепперони добавлена!
        2
        Пицца Барбекю добавлена!
        0
        Заказ подтвержен.
        """
        try:
            пункт_меню = int(пункт_меню)
            if пункт_меню == Терминал.КОМАНДА_ОТМЕНА_ЗАКАЗА:
                if self.заказ:
                    print("Заказ отменен.")
                    self.заказ = None
                else:
                    print("Нет активного заказа для отмены.")
            elif пункт_меню == Терминал.КОМАНДА_ПОДТВЕРЖДЕНИЕ_ЗАКАЗА:
                if self.заказ:
                    print("Заказ подтвержден.")
                    self.принять_оплату()
                    self.заказ.выполнить()
                    self.заказ = None
                else:
                    print("Нет активного заказа для подтверждения.")
            elif 1 <= пункт_меню <= len(self.меню):
                if not self.заказ:
                    self.заказ = Заказ()
                self.заказ.добавить(self.меню[пункт_меню - 1])
            else:
                raise ValueError
        except ValueError:
            print("Не могу распознать команду! Проверьте ввод.")
        except Exception as e:
            print(f"Во время работы терминала произошла ошибка: {e}")

    def рассчитать_сдачу(self, оплата):
        """Вернуть сдачу для 'оплата'.

        Если оплата меньше стоимости заказа, возбудить исключение ValueError.
        """
        сумма_заказа = self.заказ.сумма()
        if оплата < сумма_заказа:
            raise ValueError("Оплата меньше суммы заказа.")
        return оплата - сумма_заказа

    def принять_оплату(self):
        """Обработать оплату.

        Эмулирует оплату заказа (клиент вводит сумму с клавиатуры).

        Если сумма оплаты недостаточна (определяет метод рассчитать_сдачу())
        или возникает другая ошибка - исключние передается выше.
        """
        try:
            сумма_заказа = self.заказ.сумма()
            print(f"Сумма заказа: {сумма_заказа:.2f} р.")
            оплата = float(input("Введите сумму: "))
            сдача = self.рассчитать_сдачу(оплата)
            print(f"Вы внесли {оплата:.2f} р. Сдача: {сдача:.2f} р.")
        except Exception:
            print("Оплата не удалась. Заказ будет отменен.")
            raise