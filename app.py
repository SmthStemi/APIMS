import sys
import os
from tkinter import *
from tkinter import messagebox  # для show_text функции

def resource_path(relative_path):
    try:

        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def show_text(text):
    messagebox.showinfo("Функции", text)

def show_image(file_path):

    try:
        image_window = Toplevel(root)
        image_window.title("Изображение")

        full_path = resource_path(file_path)

        img = PhotoImage(file=full_path)
        label = Label(image_window, image=img)
        label.image = img
        label.pack()

        Button(image_window, text="Закрыть", command=image_window.destroy).pack(pady=10)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить изображение\n{str(e)}")
root = Tk()
root.geometry("500x500")

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выйти", command=root.quit)

imagemenu = Menu(mainmenu, tearoff=0)
imagemenu.add_command(label="Камера",
                      command=lambda: show_image("images/cifrkamera.png"))
imagemenu.add_command(label="Микроконтроллер",
                      command=lambda: show_image("images/Arduino.png"))
imagemenu.add_command(label="Датчик движения",
                      command=lambda: show_image("images/infradatchik.png"))
imagemenu.add_command(label="Термометр",
                      command=lambda: show_image("images/elektrtermometr.png"))

# Меню Характеристики
charkimenu = Menu(mainmenu, tearoff=0)
charkimenu.add_command(label="Камера",
                       command=lambda: show_image("images/charkikamera.png"))
charkimenu.add_command(label="Микроконтроллер",
                       command=lambda: show_image("images/charkimk.png"))
charkimenu.add_command(label="Датчики движения",
                       command=lambda: show_image("images/charkidatchik.png"))
charkimenu.add_command(label="Термометр",
                       command=lambda: show_image("images/charkiterm.png"))

functionmenu = Menu(mainmenu, tearoff=0)

functionmenu2 = Menu(functionmenu, tearoff=0)
functionmenu2.add_command(label="Инфракрасная камера",
                          command=lambda: show_text("Инфракрасная камера (тепловизор) выполняет функцию визуализации температурных различий на поверхности объектов."))
functionmenu2.add_command(label="Цифровая камера",
                          command=lambda: show_text("Цифровые камеры имеют функции, связанные со съёмкой, настройками, хранением изображений и передачей данных."))
functionmenu.add_cascade(label="Камера", menu=functionmenu2)

functionmenu3 = Menu(functionmenu, tearoff=0)
functionmenu3.add_command(label="Arduino",
                          command=lambda: show_text("Arduino - это блоки кода, которые выполняют определённую задачу. Они помогают структурировать программу, делают код более читаемым и удобным для отладки."))
functionmenu3.add_command(label="Raspberry",
                          command=lambda: show_text("Функции Raspberry Pi включают технические характеристики, работу с операционной системой, применение в проектах и программирование."))
functionmenu.add_cascade(label="Микроконтроллер", menu=functionmenu3)

functionmenu4 = Menu(functionmenu, tearoff=0)
functionmenu4.add_command(label="Инфракрасный датчик",
                          command=lambda: show_text("Инфракрасный датчик движения фиксирует тепловое (инфракрасное) излучение объектов, которые попадают в его зону действия."))
functionmenu4.add_command(label="Ультразвуковой датчик",
                          command=lambda: show_text("Ультразвуковой датчик — это электронное устройство, которое измеряет расстояние до целевого объекта путём излучения ультразвуковых волн."))
functionmenu.add_cascade(label="Датчик движения", menu=functionmenu4)

functionmenu5 = Menu(functionmenu, tearoff=0)
functionmenu5.add_command(label="Ртутный",
                          command=lambda: show_text("Ртутный термометр (градусник) выполняет функцию измерения температуры."))
functionmenu5.add_command(label="Электрический",
                          command=lambda: show_text("Электрический термометр (электронный термометр) выполняет функцию измерения температуры различных тел и сред (воздуха, почвы, воды и т. д.). Приборы могут использоваться в разных областях."))
functionmenu.add_cascade(label="Термометр", menu=functionmenu5)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Изображение", menu=imagemenu)
mainmenu.add_cascade(label="Характеристики", menu=charkimenu)
mainmenu.add_cascade(label="Функции", menu=functionmenu)

root.mainloop()