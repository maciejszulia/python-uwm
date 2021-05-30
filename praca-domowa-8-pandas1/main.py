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

# sumę dzieci urodzonych w latach 2000-2005

print(df[((df.Rok >= 2000) & (df.Rok <= 2005))].agg({'Liczba': ['sum']}))

# sumę urodzonych chłopców i dziewczynek
print('chlopcy :', df[df.Plec == 'M'].agg({'Liczba': ['sum']}))
print('dziewczynki :', df[df.Plec == 'K'].agg({'Liczba': ['sum']}))

# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(df.loc[df[df.Plec == 'M'].groupby("Rok")["Liczba"].idxmax()])
print(df.loc[df[df.Plec == 'K'].groupby("Rok")["Liczba"].idxmax()])

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
print(df.loc[df[df.Plec == 'M']['Liczba'].idxmax()])
print(df.loc[df[df.Plec == 'K']['Liczba'].idxmax()])

# Zadanie 3

a = pd.read_csv("zamowienia.csv", header=0, sep=';', decimal='.')
print(a)
print(a['Sprzedawca'].unique())
print(a.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])
print(a.groupby(['Sprzedawca']).size())
print(a.groupby(['Kraj']).agg({'Utarg': ['sum']}))
print(
    a[((a['Kraj'] == 'Polska') & (a['Data zamowienia'] >= '2005-01-01') & (a['Data zamowienia'] <= '2005-12-31'))].agg(
        {'Utarg': ['sum']}))
print(a[((a['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())
r2004 = a[((a['Data zamowienia'].str[:4] == '2004'))]
r2005 = a[((a['Data zamowienia'].str[:4] == '2005'))]
r2004.to_csv("zamowienia_2004.csv", sep=';', index=False)
r2005.to_csv("zamowienia_2005.csv", sep=';', index=False)
