# Знакомство с виджетами. Виджет Button
from cProfile import label
from cgitb import text


def say_hello():
    print('hello')


def add_label():
    label = tk.Label(win, text='new')
    label. pack()


def counter():
    global count
    count +=1
    btn4['text'] = f'Счётчик: {count}'


count = 0

import tkinter as tk

win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Моё первое графическое приложение')

btn1 = tk.Button(win, text='Hello',
                command=say_hello
                )

btn2 = tk.Button(win, text='Add new label',
                command=add_label
                )

btn3 = tk.Button(win, text='Add new label lambda',
                command=lambda: tk.Label(win, text='new lambda').pack()
                )

btn4 = tk.Button(win, text=f'Счётчик: {count}',
                command=counter,
                activebackground = 'blue',
                bg = 'green'
                )


btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()