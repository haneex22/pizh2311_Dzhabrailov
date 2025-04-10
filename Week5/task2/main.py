from writing_tools import *

if __name__ == "__main__":
    # Создаём экземпляры
    pencil = Pencil("серый", 0.5, "2B")
    pen = Pen("синяя", 0.7, "чёрные")
    gel_pen = GelPen("розовая", 1.0, "золото", True)

    # Тестируем карандаш
    print(pencil)
    pencil.write("Привет, мир!")

    # Тестируем ручку
    print(pen)
    pen.write("Привет, ООП!")

    # Тестируем гелевую ручку
    print(gel_pen)
    gel_pen.write("Это пишет гелевая ручка!")