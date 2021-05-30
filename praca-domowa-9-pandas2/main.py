from pandas import *
import xlrd
import openpyxl
from matplotlib.pyplot import *

xlsx = ExcelFile('imiona.xlsx')
a = read_excel(xlsx, header=0)
print(a)

print("Zadanie 1:")

b = a.groupby(['Rok']).agg({'Liczba' : ['sum']})
wykres = b.plot()
wykres.legend()
title("Liczba urodzonych dzieci dla każdego roku")
show()

print("Zadanie 2:")

b = a.groupby(['Plec']).agg({'Liczba' : ['sum']})
wykres = b.plot.bar()
wykres.legend()
xticks(rotation=0)
title("Liczba urodzonych chłopców i dziewcznek")
show()

print("Zadanie 3:")

b = a[a['Rok'] > 2012].groupby(['Plec']).agg({'Liczba' : ['sum']})
wykres = b.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
legend()
show()

print("Zadanie 4:")

a = read_csv('zamowienia.csv', delimiter=';')
b = a.groupby('Sprzedawca').size()
b.plot.bar()
ylabel("liczba zamówień")
show()