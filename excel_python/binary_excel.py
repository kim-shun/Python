import openpyxl as excel

book = excel.Workbook()
sheet = book.active


num = int(input("整数を入力してください:"))

sheet["B2"] = num
sheet["C2"] = format(num,'b')


file_template = "binary_excel.xlsx"
book.save(file_template)
