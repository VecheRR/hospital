import tkinter as tk
from tkinter import filedialog as fd


def select_file():
    filetypes = (
        ('text files', '*.csv')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',)
        #filetypes=filetypes)


window = tk.Tk()

frame1 = tk.Frame(master=window, width=360, height=480)
frame1.pack()

select_csv = tk.Button(master=window, text="CSV", command=select_file)
select_csv.pack()

window.mainloop()