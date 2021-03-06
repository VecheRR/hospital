# Created by Vladislav Vecherkovsky.
# Date: 7.03.2022
# Code generating 184 PDF-pages for 1.0846281051635742 seconds.
# It means for 1 PDF-page in average spending 0,005894717963 seconds.
# Results was received on MacBook Pro 13 M1 8Gb

import csv
import datetime

from functions import functions
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog as fd


def select_file():
    filetypes = (
        ('text files', '*.csv')
    )
    global filename
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/')

    print(filename)
    # window.destroy()


dic = {}
window = tk.Tk()


def g1():
    # text = entry.get(1.0, tk.END).split('\n')[:-1]
    # #if text[0] == '':
    #   #  return
    #
    # for row in text:
    #     row = row.split(' = ')
    #     print(row)
    #     dic[row[0]] = row[1]
    #
    # print(dic)

    global t1, t2, t3, t4
    t1 = entry1.get()
    t2 = entry2.get()
    t3 = entry3.get()
    t4 = entry4.get()

    if t1 == '':
        t1 = '-'
    if t2 == '':
        t2 = '-'
    if t3 == '':
        t3 = '-'
    if t4 == '':
        t4 = '-'

    window.destroy()


def f2(dicti):
    # if len(dicti) == 0:
    #     return
    for key in dicti.keys():
        f(key, dicti)


frame1 = tk.Frame(master=window)
frame1.pack()

select_csv = tk.Button(master=window, text="CSV", command=select_file)
select_csv.pack()

# lab = tk.Label(master=window, text="Введите <ключ = значение>")
# lab.pack()

# entry = tk.Text(master=window, height=10, width=40, font=("Veranda", 24, 'bold'))
# entry.pack()

lab1 = tk.Label(master=window, text="Юрид лицо направившее материал")
lab1.pack()

entry1 = tk.Entry(master=window, font=("Veranda", 24, 'bold'))
entry1.pack()


lab2 = tk.Label(master=window, text="Фио врача направившего материал")
lab2.pack()

entry2 = tk.Entry(master=window, font=("Veranda", 24, 'bold'))
entry2.pack()


lab3 = tk.Label(master=window, text="Отделение")
lab3.pack()

entry3 = tk.Entry(master=window, font=("Veranda", 24, 'bold'))
entry3.pack()


lab4 = tk.Label(master=window, text="Палата")
lab4.pack()

entry4 = tk.Entry(master=window, font=("Veranda", 24, 'bold'))
entry4.pack()

btn = tk.Button(master=window, command=g1, text="Done")
btn.pack()

window.mainloop()

k = {"Юр лицо напр материал": t1, "Фио врача напр материал": t2, "Отделение": t3, "Палата": t4}
########################################################################################
file = open(filename)
file2 = open(filename)

print("Получено!")

csvreader = csv.reader(file)
csvreader2 = csv.reader(file2)

pdf = FPDF()

header = functions.get_row(csvreader)
header[0] = "№ заказа"

# header.append("1")
# header.append("2")
# header.append("3")
# header.append("From")

w = 191


def f(name, d):
    if name == "Пол":
        d[name] = "Мужской" if d[name] == "1" else "Женский"

    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, f'{name}:', align="L", border=0)

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(110, 5, f'{d[name]}', align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)


def call_f(sp, d):
    for el in sp:
        f(el, d)


def create_page():
    pdf.add_page()
    pdf.add_font('Times-Roman', '', 'src/ofont.ru_Times New Roman.ttf', uni=True)
    pdf.add_font('Times-Roman-Bold', '', 'src/BOLDTimes New Roman.ttf', uni=True)
    pdf.set_font("Times-Roman", size=20)
    pdf.set_text_color(0, 0, 0)


def fill_top_page():
    pdf.multi_cell(w, 10, txt='ГБУЗ РА «Адыгейская республиканская клиническая инфекционная больница»', align="C")

    pdf.set_font("Times-Roman", size=11)
    pdf.multi_cell(w, 10, 'Юридический адрес: 385017, Республика Адыгея, г. Майкоп, ул. 2-я Короткая, д. 8',
                   align="C")

    pdf.multi_cell(w, 10, 'Телефон / факс: 8(8772) 54-67-62 / 54-98-85 ОКПО 24441619 ОГРН 1020100708330', align="C")

    pdf.multi_cell(w, 10, 'ИНН 0105020580 КПП 010501001', align="C")

    pdf.multi_cell(w, 10, 'Лицензия «На осущствление медицинской деятельности» от 8.11.2018 № ЛО-01-01-000604',
                   align="C")


def fill_mid_page():
    data = functions.get_row(csvreader)
    d = dict(zip(header, data))
    print(d)

    global rez
    rez = d["Результат"]

    months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
              "07": "июля",
              "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}
    date = d["Дата готовности результата"].split('-')

    pdf.multi_cell(w, 10, f'№ {d["№ заказа"]} от «{date[2]}» {months[date[1]]}', align="C")

    t = 110

    pdf.set_draw_color(192, 192, 192)

    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, 'ФИО обследуемого:', align="L", border=0)

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(t, 5, f'{d["Фамилия"]} {d["Имя"]} {d["Отчество"]}', align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)

    call_f(['Дата рождения'], d)
    # print(data[-1])

    dd = {"Юр лицо направившее пробу": data[-1]}
    f2(dd)

    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, 'Адрес обследуемого:', align="L", border=0)

    g = [d["Адрес факт город"], d["Адрес факт улица"],
         d["Адрес факт дом"], d["Адрес факт строение"], d["Адрес факт квартира"]]

    # for i in range(len(g)):
    #     if g[i] == '-':
    #         g[i] = ''

    text = f'г. {g[0]}, ул. {g[1]}, дом {g[2]}, стр. {g[3]}, квар. {g[4]}'

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(t, 5, text, align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)

    call_f(['Телефон', 'Дата взятия биоматериала', 'Дата готовности результата', 'Тип ДУЛ', 'Номер документа', 'Серия документа', 'СНИЛС', 'ОМС'], d)


def fill_bot_page():
    b = 1
    pdf.set_draw_color(150, 150, 150)
    pdf.set_font("Times-Roman-Bold", size=10)

    pdf.x += 25
    pdf.y += 7
    tmp = pdf.y
    pdf.multi_cell(40, 5, f'Определяемый показатель', align="C", border=b)

    pdf.x += 65
    pdf.y = tmp
    pdf.multi_cell(30, 5, f'Допустимые уровни', align="C", border=b)

    pdf.x += 95
    pdf.y = tmp
    pdf.multi_cell(30, 5, f'Результат исследования', align="C", border=b)

    pdf.x += 125
    pdf.y = tmp
    pdf.multi_cell(40, 5, f'НД на метод исследования', align="C", border=b)

    pdf.set_font("Times-Roman", size=10)

    pdf.x += 25
    # pdf.y += 7
    tmp = pdf.y
    pdf.multi_cell(40, 5, f'РНК коронавируса 2019-nCoV', align="L", border=b)

    pdf.x += 65
    pdf.y = tmp
    pdf.multi_cell(30, 10, f'Не допускается', align="L", border=b)

    ans = ""
    if rez == "0":
        ans = "Не обнаружено"
    if rez == "1":
        ans = "Обнаружено"
    if rez == "2":
        ans = "Сомнительно"
    if rez == "3":
        ans = "Брак"

    pdf.x += 95
    pdf.y = tmp
    pdf.multi_cell(30, 10, f'{ans}', align="L", border=b)

    pdf.set_font("Times-Roman", size=8)

    pdf.x += 125
    pdf.y = tmp
    pdf.multi_cell(40, 3.33, f'Руководство по приминению набора реагентов для обнаружения «SARS-CoV-2»', align="L",
                   border=b)

    pdf.set_font("Times-Roman", size=10)

    pdf.x += 10
    pdf.multi_cell(60, 5, "Сведения о средствах измерения:")

    pdf.x += 10
    pdf.multi_cell(w, 5,
                   "Прибор для проведения полимеразной цепной реакции «QuantStudio5» SN277710568, REF F43321, "
                   "от 04.01.2021", align="L")

    pdf.x += 10
    pdf.multi_cell(w, 5, "Амплификатор детектирующий ДТпрайм 5М1. Заводской номер: А51552. Произовдитель: ООО «НПО ДНК-Технологии»")

    # pdf.x += 10
    # pdf.multi_cell(w, 5,
    #                "QuantStudio")

def all_steps():
    create_page()
    fill_top_page()
    fill_mid_page()
    f2(k)
    f2(dic)
    fill_bot_page()


for i in range(functions.col(csvreader2) - 2):
    print(i)
    all_steps()

pdf.output(f"{datetime.datetime.now()}.pdf")
