import datetime

books_num = 18
notebooks_num = 23
pens_num = 9
books_sold = int(input("how many books you sold:\n"))
notebooks_sold = int(input("how many notebooks you sold:\n"))
pens_sold = int(input("how many pens you sold:\n"))
books_left = books_num - books_sold
notebooks_left = notebooks_num - notebooks_sold
pens_left = pens_num - pens_sold
print("books left", books_left)
print("notebooks left", notebooks_left)
print("pens left", pens_left)
print("date of today", datetime.date.today())
updated_stock_books = books_left + 4
updated_stock_notebooks = notebooks_left + 2
updated_stock_pens = pens_left + 5

print("the updated stock after the purchase in ", datetime.datetime.now())
print("updated num of books: ", updated_stock_books)
print("updates num of notebooks: ", updated_stock_notebooks)
print("updated num of pens: ", updated_stock_pens)
# first purchase
print("enter the date of the first purchase:")
year1 = int(input("year: "))
month1 = int(input("month: "))
day1 = int(input("day: "))
books1 = int(input("num of books: "))
notebooks1 = int(input("num of notebooks: "))
pens1 = int(input("num of pens: "))
date1 = datetime.date(year1, month1, day1)
# second purchase
print("enter the date of the second purchase:")
year2 = int(input("year: "))
month2 = int(input("month: "))
day2 = int(input("day: "))
books2 = int(input("num of books: "))
notebooks2 = int(input("num of notebooks: "))
pens2 = int(input("num of pens: "))
date2 = datetime.date(year2, month2, day2)
# comparison- which purchse happened first
print("does the first purchase happened before the second purchase?: ", date1 < date2)
# the current stock after all the purchases
books_stock = updated_stock_books - books1 - books2
notebooks_stock = updated_stock_notebooks - notebooks1 - notebooks2
pens_stock = updated_stock_pens - pens1 - pens2
print("the current stock:")
print("books:", books_stock)
print("notebooks:", notebooks_stock)
print("pens: ", pens_stock)
