import numpy as np
import pandas as pd
import xlrd
import openpyxl

# Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce
# dostępny w pliku /datasets/imiona.xlsx

imiona = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(imiona)
print(df)

# Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku

print(df[df['Liczba'] > 1000])

# tylko rekordy gdzie nadane imię jest takie jak Twoje

print(df[df['Imie'] == 'MACIEJ'])

# sumę wszystkich urodzonych dzieci w całym danym okresie,

print(df.agg({'Liczba': ['sum']}))
