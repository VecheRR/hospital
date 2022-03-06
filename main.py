# Crated by Vladislav Vecherkosvky at 5 March 2022

import csv
from functions import functions
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

file = open('src/table.csv')

# try:
#     file = open(functions.xlsx_to_csv('src/test.xlsx'))
# except TypeError:
#     pass
#
# print(123)

csvreader = csv.reader(file)

header = functions.get_row(csvreader)
header[0] = "№ заказа"

data = functions.get_row(csvreader)

# print(data)
# print(header)

d = dict(zip(header, data))

pdf = FPDF()
pdf.add_page()
pdf.add_font('Times-Roman', '', 'src/ofont.ru_Times New Roman.ttf', uni=True)
pdf.add_font('Times-Roman-Bold', '', 'src/BOLDTimes New Roman.ttf', uni=True)
pdf.set_font("Times-Roman", size=20)
pdf.set_text_color(0, 0, 0)

w = 191

pdf.multi_cell(w, 10, txt='ГБУЗ РА «Адыгейская республиканская клиническая инфекционная больница»', align="C")

pdf.set_font("Times-Roman", size=11)
pdf.multi_cell(w, 10, 'Юридический адрес: 385017, Республика Адыгея, г. Майкоп, ул. 2-я Короткая, д. 8', align="C")

pdf.multi_cell(w, 10, 'Телефон / факс: 8(8772) 54-67-62 / 54-98-85 ОКПО 24441619 ОГРН 1020100708330', align="C")

pdf.multi_cell(w, 10, 'ИНН 0105020580 КПП 010501001', align="C")

pdf.multi_cell(w, 10, 'Лицензия «На осущствление медицинской деятельности» от 8.11.2018 № ЛО-01-01-000604', align="C")

# pdf.multi_cell(w, 10, '', align="C")

months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня", "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}
date = d["Дата готовности результата"].split('-')

pdf.multi_cell(w, 10, f'№ {d["№ заказа"]} от «{date[2]}» {months[date[1]]}', align="C")

t = 110

pdf.set_draw_color(192, 192, 192)


def f(name):
    pdf.x += 10
    tmp = pdf.y
    pdf.multi_cell(60, 5, f'{name}:', align="L", border=0)

    pdf.x += 70
    pdf.y = tmp
    pdf.multi_cell(t, 5, f'{d[name]}', align="L", border=0)

    pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)


pdf.x += 10
tmp = pdf.y
pdf.multi_cell(60, 5, 'ФИО обследуемого:', align="L", border=0)

pdf.x += 70
pdf.y = tmp
pdf.multi_cell(t, 5, f'{d["Фамилия"]} {d["Имя"]} {d["Отчество"]}', align="L", border=0)

pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)

f('Пол')

f('Дата рождения')


pdf.x += 10
tmp = pdf.y
pdf.multi_cell(60, 5, 'Адрес обследуемого:', align="L", border=0)

g = [d["Адрес регистрации город"], d["Адрес регистрации улица"],
     d["Адрес регистрации дом"], d["Адрес регистрации строение"], d["Адрес регистрации квартира"]]

for i in range(len(g)):
    if g[i] == '-':
        g[i] = ''

text = f'г. {g[0]}, ул. {g[1]}, дом {g[2]}, стр. {g[3]}, квар. {g[4]}'


pdf.x += 70
pdf.y = tmp
pdf.multi_cell(t, 5, text, align="L", border=0)

pdf.line(pdf.x + 10, pdf.y, pdf.x + 175, pdf.y)

f('Телефон')

# Номер документа;Серия документа;СНИЛС;ОМС;
# Дата заказа;Код услуги;Название услуги;Тест-система;Дата взятия б-м;
# Дата готовности результата;Результат;Тип исследования;Значение результата;

f('Код услуги')

f('Дата заказа')

f('Название услуги')

f('Тест-система')

f('Дата взятия б-м')

f('Дата готовности результата')

# f('Результат')

f('Тип исследования')

f('Значение результата')

f('Тип ДУЛ')

f('Номер документа')

f('Серия документа')

f('СНИЛС')

f('ОМС')


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



pdf.output("simple_demo.pdf")




exit()


# print(d)

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
pdfmetrics.registerFont(TTFont('Times-Roman', 'src/ofont.ru_Times New Roman.ttf'))
can.setFont('Times-Roman', 11)
can.setFillColorRGB(1, 0, 0)

months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня", "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}
date = d["Дата готовности результата"].split('-')
print(date)

can.drawString(203, 628, f'№ {d["№ заказа"]} от «{date[1]}» {months[date[2]]}')

can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)

existing_pdf = PdfFileReader(open("src/basic.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
