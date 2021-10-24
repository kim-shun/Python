import openpyxl as excel

book = excel.Workbook()
sheet = book.active

num = int(input("整数を入力してください:"))
sheet["C2"] = format(num,'b')

book.save("binary_excel.xlsx")
