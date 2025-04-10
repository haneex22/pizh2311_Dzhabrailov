class WritingTool:
    """Базовый класс для пишущих принадлежностей."""
    
    def __init__(self, color: str, thickness: float):
        self._color = color          # Цвет инструмента (защищённое поле)
        self._thickness = thickness  # Толщина линии (защищённое поле)
        self.__durability = 100      # Степень износа (приватное поле)

    def write(self, text: str) -> None:
        """Метод для написания текста."""
        print(f"Пишем: '{text}' | Цвет: {self._color}, Толщина: {self._thickness} мм")
        self._clean_tip()

    def _clean_tip(self) -> None:
        """Защищённый метод для очистки стержня."""
        print("Стержень очищен (базовый метод)")

    def __str__(self):
        return f"Инструмент: цвет={self._color}, толщина={self._thickness}"


class Pencil(WritingTool):
    """Класс карандаша."""
    
    def __init__(self, color: str, thickness: float, hardness: str):
        super().__init__(color, thickness)
        self._hardness = hardness  # Твёрдость грифеля (защищённое поле)

    def write(self, text: str) -> None:
        """Переопределённый метод для карандаша."""
        print(f"(Карандаш) Рисуем: '{text}' | Твёрдость: {self._hardness}")
        super()._clean_tip()


class Pen(WritingTool):
    """Класс ручки."""
    
    def __init__(self, color: str, thickness: float, ink_color: str):
        super().__init__(color, thickness)
        self.__ink_color = ink_color  # Цвет чернил (приватное поле)

    def write(self, text: str) -> None:
        """Переопределённый метод для ручки."""
        print(f"(Ручка) Пишем: '{text}' | Чернила: {self.__ink_color}")


class GelPen(Pen):
    """Класс гелевой ручки."""
    
    def __init__(self, color: str, thickness: float, ink_color: str, glitter: bool):
        super().__init__(color, thickness, ink_color)
        self._glitter = glitter  # Наличие блёсток (защищённое поле)

    def write(self, text: str) -> None:
        """Переопределённый метод для гелевой ручки."""
        if self._glitter:
            print(f"(Гелевая ручка) Блестящий текст: '{text}' ")
        else:
            super().write(text)