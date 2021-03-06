# Crated by Vladislav Vecherkosvky. 5 March 2022

import csv
from functions import functions
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import time

t1 = time.time()

# file = open('src/table.csv')
file = open('src/test2.csv')
file2 = open('src/test2.csv')

# file = open('src/test.xlsx')

# file = functions.xlsx_to_csv("src/table.csv")

csvreader = csv.reader(file)
csvreader2 = csv.reader(file2)

header = functions.get_row(csvreader)
header[0] = "№ заказа"

# data = functions.get_row(csvreader)

pdf = FPDF()


w = 191


def f(name, d):
    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, f'{name}:', align="L", border=0)

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(110, 5, f'{d[name]}', align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)


def all_pdf():
    data = functions.get_row(csvreader)

    d = dict(zip(header, data))

    pdf.add_page()
    pdf.add_font('Times-Roman', '', 'src/ofont.ru_Times New Roman.ttf', uni=True)
    pdf.add_font('Times-Roman-Bold', '', 'src/BOLDTimes New Roman.ttf', uni=True)
    pdf.set_font("Times-Roman", size=20)
    pdf.set_text_color(0, 0, 0)

    pdf.multi_cell(w, 10, txt='ГБУЗ РА «Адыгейская республиканская клиническая инфекционная больница»', align="C")

    pdf.set_font("Times-Roman", size=11)
    pdf.multi_cell(w, 10, 'Юридический адрес: 385017, Республика Адыгея, г. Майкоп, ул. 2-я Короткая, д. 8', align="C")

    pdf.multi_cell(w, 10, 'Телефон / факс: 8(8772) 54-67-62 / 54-98-85 ОКПО 24441619 ОГРН 1020100708330', align="C")

    pdf.multi_cell(w, 10, 'ИНН 0105020580 КПП 010501001', align="C")

    pdf.multi_cell(w, 10, 'Лицензия «На осущствление медицинской деятельности» от 8.11.2018 № ЛО-01-01-000604',
                   align="C")

    # pdf.multi_cell(w, 10, '', align="C")

    months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня", "07": "июля",
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

    f('Пол', d)

    f('Дата рождения', d)

    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, 'Адрес обследуемого:', align="L", border=0)

    g = [d["Адрес факт город"], d["Адрес факт улица"],
         d["Адрес факт дом"], d["Адрес факт строение"], d["Адрес факт квартира"]]

    for i in range(len(g)):
        if g[i] == '-':
            g[i] = ''

    text = f'г. {g[0]}, ул. {g[1]}, дом {g[2]}, стр. {g[3]}, квар. {g[4]}'

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(t, 5, text, align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)

    f('Телефон', d)

    # Номер документа;Серия документа;СНИЛС;ОМС;
    # Дата заказа;Код услуги;Название услуги;Тест-система;Дата взятия б-м;
    # Дата готовности результата;Результат;Тип исследования;Значение результата;

    f('Код услуги', d)

    f('Дата заказа', d)

    f('Название услуги', d)

    f('Тест-система', d)

    f('Дата взятия биоматериала', d)

    f('Дата готовности результата', d)

    # f('Результат')

    f('Тип исследования', d)

    f('Значение результата', d)

    f('Тип ДУЛ', d)

    f('Номер документа', d)

    f('Серия документа', d)

    f('СНИЛС', d)

    f('ОМС', d)

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

    pdf.x += 95
    pdf.y = tmp
    pdf.multi_cell(30, 10, f'{d["Результат"]}', align="L", border=b)

    pdf.set_font("Times-Roman", size=8)

    pdf.x += 125
    pdf.y = tmp
    pdf.multi_cell(40, 2.5, f'Руководство по приминению набора реагентов «АмплиПрайм SARS-CoV-2 DUO»', align="L", border=b)

    pdf.set_font("Times-Roman", size=10)

    pdf.x += 10
    pdf.multi_cell(60, 5, "Сведения о средствах измерения:")

    pdf.x += 10
    pdf.multi_cell(w, 5, "Прибор для проведения полимеразной цепной реакции «QuantStudio5» SN277710568, REF F43321, "
                         "от 04.01.2021", align="L")

    pdf.x += 10
    pdf.multi_cell(w, 5, "Дата проведения исследований: с 05.03.2022 8:35 по 05.03.2022")


for i in range(functions.col(csvreader2) - 2):
    print(i)
    all_pdf()

pdf.output("simple_demo.pdf")

t2 = time.time()