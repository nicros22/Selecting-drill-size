from tkinter import *
from tkinter.ttk import Combobox
from data import dict

def button_clicked():
    first = combo1.get()
    second = combo2.get()
    third = combo3.get()
    fourth = combo4.get()
    index = dict[third].index(fourth)
    drill_diameter = dict[third][index + 1]
    if second == 'Чугун' or second == 'Бронза' or second == 'Пластмасса':
        drill_diameter = round(float(drill_diameter) - 0.1, 3)
    answer_lbl = Label(root, text=f"Ответ: {drill_diameter} ")
    answer_lbl.grid(row=5, column=0)

def change_combo(*args):
    first = combo1.get()
    second = combo2.get()
    third = combo3.get()
    fourth = combo4.get()
    result = []
    for i, value in enumerate(dict[third]):
        if i % 2 == 0:
            result.append(value)

    combo4['values'] = result

    if first == 'Метрическая':
        combo3['values'] = list(dict.keys())
    elif first == 'Дюймовая':
        combo3['values'] = ['В доработке']


root = Tk()
root.geometry("800x500")
root.title("Выбор сверла")

combo1_lbl = Label(root, text="Выберите тип")
combo1_lbl.grid(row=0, column=1)

combo2_lbl = Label(root, text="Выберите материал")
combo2_lbl.grid(row=1, column=1)

combo3_lbl = Label(root, text="Выберите размер")
combo3_lbl.grid(row=2, column=1)

combo4_lbl = Label(root, text="Выберите шаг")
combo4_lbl.grid(row=3, column=1)

combo1 = Combobox(root, values=['Метрическая', 'Дюймовая'], state='readonly')
combo1.current(0)
combo1.bind("<<ComboboxSelected>>", change_combo)
combo1.grid(row=0, column=0)

combo2 = Combobox(root, values=['Сталь', 'Латунь', 'Алюминий', 'Чугун', 'Бронза', 'Пластмасса'], state='readonly')
combo2.current(0)
combo2.bind("<<ComboboxSelected>>", change_combo)
combo2.grid(row=1, column=0)

combo3 = Combobox(root, values=['2', '2', '3'], state='readonly')
combo3.current(0)
combo3.bind("<<ComboboxSelected>>", change_combo)
combo3.grid(row=2, column=0)

combo4 = Combobox(root, values=[], state='readonly')
combo4.grid(row=3, column=0)

button = Button(root, text="Посчитать", command=button_clicked)
button.grid(row=4, column=0)



root.mainloop()

