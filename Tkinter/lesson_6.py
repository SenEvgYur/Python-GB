# Создаём калькулятор

import tkinter as tk


def add_number(number):
    value = calc.get() + str(number)
    calc.delete(0, tk.END)
    calc.insert(0, value)

win = tk.Tk()
win.geometry(f'240x260+100+200')
win['bg'] = '#33ffe6'
win.title('Калькулятор')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=0, column=0, columnspan=3, sticky='we')

tk.Button(text='1', bd=5, font=('Arial', 13), command=lambda : add_number(1)).grid(row=1, column=0, sticky='wens', padx=5, pady=5)
tk.Button(text='2', bd=5, font=('Arial', 13), command=lambda : add_number(2)).grid(row=1, column=1, sticky='wens', padx=5, pady=5)
tk.Button(text='3', bd=5, font=('Arial', 13), command=lambda : add_number(3)).grid(row=1, column=2, sticky='wens', padx=5, pady=5)
tk.Button(text='4', bd=5, font=('Arial', 13), command=lambda : add_number(4)).grid(row=2, column=0, sticky='wens', padx=5, pady=5)
tk.Button(text='5', bd=5, font=('Arial', 13), command=lambda : add_number(5)).grid(row=2, column=1, sticky='wens', padx=5, pady=5)
tk.Button(text='6', bd=5, font=('Arial', 13), command=lambda : add_number(6)).grid(row=2, column=2, sticky='wens', padx=5, pady=5)
tk.Button(text='7', bd=5, font=('Arial', 13), command=lambda : add_number(7)).grid(row=3, column=0, sticky='wens', padx=5, pady=5)
tk.Button(text='8', bd=5, font=('Arial', 13), command=lambda : add_number(8)).grid(row=3, column=1, sticky='wens', padx=5, pady=5)
tk.Button(text='9', bd=5, font=('Arial', 13), command=lambda : add_number(9)).grid(row=3, column=2, sticky='wens', padx=5, pady=5)
tk.Button(text='0', bd=5, font=('Arial', 13), command=lambda : add_number(0)).grid(row=4, column=0, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()