import tkinter as tk
from tkinter import filedialog as fd

dic = {"Напр врач": ""}


def g():
    text = entry.get(1.0, tk.END).split('\n')[:-1]

    for row in text:
        row = row.split(' = ')
        print(row)
        dic[row[0]] = row[1]

    print(dic)


window = tk.Tk()

frame1 = tk.Frame(master=window)
frame1.pack()

# entry = tk.Text(master=window, height=20, width=80, font=("Veranda", 24, 'bold'))
# entry.pack()

lab1 = tk.Label(master=window, )

entry1 = tk.Entry(master=window, font=("Veranda", 24, 'bold'))
entry1.pack()

btn = tk.Button(master=window, command=g, text="Done")
btn.pack()

window.mainloop()

# TODO:
# Добавить entry's и имена к ним. Делать локальный словарь и отправлять его в f(),
# чтобы не засорять таблицу, пихая в каждого человека дефольное значение.
