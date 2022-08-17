# tkinter
# from tkinter import *
# -*- coding: utf-8 -*-

import tkinter as tk


def save(a, b, c):
    surname = a.get()
    name = b.get()
    surname2 = c.get()
    with open('file1.txt', 'a', encoding='utf-8') as data:
        data.write(surname + ' ' + name + ' ' + surname2 + '\n')


window = tk.Tk()
window.geometry('400x250')
window.title("Регистрация")


label = tk.Label(text="Введите имя", font=("Arial Bold", 14))
name = tk.Entry()
label.grid(column=0, row=1)
name.grid(
    column=1,
    row=1,
    padx=10,
    pady=10,
    ipadx=40,
    ipady=5
)

label = tk.Label(text="Введите фамилию", font=("Arial Bold", 14))
surname = tk.Entry()
label.grid(column=0, row=2)
surname.grid(
    column=1,
    row=2,
    padx = 10,
    pady = 10,
    ipadx = 40,
    ipady = 5
)

label = tk.Label(text="Введите отчество", font=("Arial Bold", 14))
surname2 = tk.Entry()
label.grid(column=0, row=3)
surname2.grid(
    column=1,
    row=3,
    padx=10,
    pady=10,
    ipadx=40,
    ipady=5
)

button = tk.Button(
    text="Сохранить",
    padx=10,
    pady=10,
    bg='#808080',
    fg="white",
    command=lambda: save(surname, name, surname2)
)
button.grid(column=1, row=4)

window.mainloop()