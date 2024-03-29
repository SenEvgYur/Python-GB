# Калькулятор для пользователя с интерфейсом

import tkinter as tk


def add_number(number):
    value = calc.get()
    if value[0] == '0':  # and len(value) == 1
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + number)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    # elif '+' in value or '-' in value or '/' in value or '*' in value:
    #     calculate()
    #     value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def make_number_button(number):
    return tk.Button(text=number,
                     bd=5,
                     font=('Arial', 13),
                     command=lambda: add_number(number))


def make_operation_button(operation):
    return tk.Button(text=operation,
                     bd=5,
                     font=('Arial', 13),
                     fg='red',
                     command=lambda: add_operation(operation))


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def make_calc_button(operation):
    return tk.Button(text=operation,
                     bd=5,
                     font=('Arial', 13),
                     fg='red',
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation,
                     bd=5,
                     font=('Arial', 13),
                     fg='red',
                     command=clear)


win = tk.Tk()
win.geometry(f'240x270+100+200')
win['bg'] = '#33ff5f'
win.title('Калькулятор')

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

make_number_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_number_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_number_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_number_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_number_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_number_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_number_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_number_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_number_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_number_button('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()