# Знакомство с виджетами. Виджет Label

from cProfile import label
import tkinter as tk

win = tk.Tk()
win.geometry('300x400+100+100')
win.title('Моё первое графическое приложение')
label_1 = tk.Label(win, text = '''Hello 
                    world!''',
                    bg = 'red', # Back Ground
                    fg = 'white', # Font Ground
                    font = ('Arial', 15, 'bold'), # шрифт лэйбла
                    # padx = 30, # отступы внутри окна
                    # pady = 40 # отступы внутри окна
                    width = 20, # ширина лэйбла
                    height = 10, # высота лэйбла
                    anchor = 'sw', # расположение лейбла внутри своего окна, по сторонам света
                    relief = tk.RAISED, # рельеф окна
                    bd = 10, # ширина рельефа окна
                    justify = tk.RIGHT # выравнивание текста
                    )
label_1.pack()

win.mainloop()