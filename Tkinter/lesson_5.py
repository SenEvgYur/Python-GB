# Знакомство с виджетами. Виджет Entry


import tkinter as tk

win = tk.Tk()
win.geometry('300x400+100+100')
win.title('Моё первое графическое приложение')

for i in range(5):
    for j in range(2):
        tk.Button(win, text = f'Hello {i} {j}').grid(row=i, column=j, stick='we')


win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()