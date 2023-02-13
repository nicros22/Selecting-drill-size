from tkinter import *
from tkinter.ttk import Combobox


def button_clicked():
    print("Button clicked")
    answer_lbl = Label(root, text="Ответ")
    answer_lbl.grid(row=5, column=0)

def change_combo(*args):
    first = combo1.get()
    second = combo2.get()
    third = combo3.get()

    if first == 'Option 1' and second == 'Sub-Option 1' and third == 'Choice 1':
        combo4['values'] = ['Result 1', 'Result 2', 'Result 3']
    elif first == 'Option 2' and second == 'Sub-Option 4' and third == 'Choice 2':
        combo4['values'] = ['Result 4', 'Result 5', 'Result 6']
    elif first == 'Option 3' and second == 'Sub-Option 7' and third == 'Choice 3':
        combo4['values'] = ['Result 7', 'Result 8', 'Result 9']
    else:
        combo4['values'] = []
    combo4.current(0)

root = Tk()
root.geometry("800x500")
root.title("Выбор сверла")

combo1_lbl = Label(root, text="Выберите тип")
combo1_lbl.grid(row=0, column=1)

combo2_lbl = Label(root, text="Выберите материал")
combo2_lbl.grid(row=1, column=1)

combo3_lbl = Label(root, text="Выберите размер")
combo3_lbl.grid(row=2, column=1)

combo3_lbl = Label(root, text="Выберите шаг")
combo3_lbl.grid(row=3, column=1)

combo1 = Combobox(root, values=['Метрическая', 'Дюймовая'], state='readonly')
combo1.current(0)
combo1.bind("<<ComboboxSelected>>", change_combo)
combo1.grid(row=0, column=0)

combo2 = Combobox(root, values=['Сталь', 'Латунь', 'Алюминий', 'Чугун', 'Бронза', 'Пластмасса'], state='readonly')
combo2.current(0)
combo2.bind("<<ComboboxSelected>>", change_combo)
combo2.grid(row=1, column=0)

combo3 = Combobox(root, values=['Choice 1', 'Choice 2', 'Choice 3'], state='readonly')
combo3.current(0)
combo3.bind("<<ComboboxSelected>>", change_combo)
combo3.grid(row=2, column=0)

combo4 = Combobox(root, values=[], state='readonly')
combo4.grid(row=3, column=0)

button = Button(root, text="Посчитать", command=button_clicked)
button.grid(row=4, column=0)



root.mainloop()

