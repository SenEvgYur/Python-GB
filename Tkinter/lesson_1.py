# Введение в tkinter. Главное окно

import tkinter as tk

win = tk.Tk()

photo = tk.PhotoImage(file = 'joystick.png')
win.iconphoto(False, photo)
win.config(bg = '#00FF5E')
win.title('Моё первое графическое приложение')
win.geometry('500x500+100+100')
win.minsize(400, 300)
win.maxsize(900, 800)
win.resizable(True, True) # Отвечает за способность изменять размеры окна
win.mainloop()