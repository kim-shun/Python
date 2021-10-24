import openpyxl as excel

book = excel.Workbook()
sheet = book.active


for i in range(5):
    num = int(input("整数を入力してください:"))
    sheet.cell(row=i + 2, column=2).value = num
    sheet.cell(row=i + 2, column=3).value = format(num,'b')
    sheet.cell(row=i + 2, column=4).value = hex(num)


file_template = "binary_excel.xlsx"
book.save(file_template)
