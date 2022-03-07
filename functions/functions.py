import csv
import xlrd
import openpyxl


def get_row(csvreader):
    data = []
    data = next(csvreader)

    # print(data)

    data = data[0].split(';')
    # data[0] = '№ заказа'

    # data = list(filter(lambda x: x != "", data))
    data = data[:42]



    for i in range(len(data)):
        if data[i] == '':
            data[i] = '-'

    return data


def csv_from_excel(xls_name):
    wb = xlrd.open_workbook('src/test.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
    return your_csv_file


def xlsx_to_csv(xlsx_name):
    xlsx = openpyxl.load_workbook(xlsx_name)

    # opening the active sheet
    sheet = xlsx.active

    # getting the data from the sheet
    data = sheet.rows

    # creating a csv file
    csv = open("data.csv", "w+")

    for row in data:
        l = list(row)[:38]
        cnt = 0
        for i in range(len(l)):
            if l[i].value is None:
                cnt += 1
            if i == len(l) - 1:
                csv.write(str(l[i].value))
            else:
                csv.write(str(l[i].value) + ',')
            csv.write('\n')
        if cnt == 38:
            break

    # close the csv file
    # csv.close()

    return csv


def col(reader):
    len_csv = 0
    for row in reader:
        len_csv += 1
        n = row[0].split(";")
        if n[0] == "":
            break

    return len_csv
