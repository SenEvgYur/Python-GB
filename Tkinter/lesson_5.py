# Знакомство с виджетами. Виджет Entry


import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0, tk.END)

def submite_entry():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)

win = tk.Tk()
win.geometry('400x400+100+100')
win.title('Моё первое графическое приложение')
tk.Label(win, text='Имя').grid(row=0, column=0, sticky='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, sticky='w')
name = tk.Entry(win)
password = tk.Entry(win, show='*')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')
tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, sticky='we')
tk.Button(win, text='submite', command=submite_entry).grid(row=3, column=1, sticky='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello'))\
    .grid(row=2, column=2, sticky='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()