# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz
# po dwie zmienne każdego typu a następnie wyświetl te zmienne

# MACIEJ SZULIA 154733

print("zadanie1: \n")

a = 10
aa = 20
b = 20.1
bb = 20.2
c = 'string'
cc = 'string2'
d = (3 + 1j)
dd = (3 + 2j)

zmienne = [a, aa, b, bb, c, cc, d, dd]

for x in range(8):
    print(zmienne[x])

for x in range(8):
    print(type(zmienne[x]))

# Zad2. Stwórz skrypt kalkulator,
# w którym wykorzystać wszystkie podstawowe działania arytmetyczne


a = 10
aa = 20
b = 20.1
bb = 20.2
c = 'string'
cc = 'string2'
d = (3 + 1j)
dd = (3 + 2j)


def dodawanie(a, b):
    return (a + b)


def mnozenie(a, b):
    return (a * b)


def dzielenie(a, b):
    return (a / b)


def odejmowanie(a, b):
    return (a - b)


dzialania = [
    dodawanie(a, b),
    mnozenie(a, b),
    dzielenie(a, b),
    odejmowanie(a, b)
]

for x in range(4):
    print(dzialania[x])

# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %


a,b,c,d,e,d,f,g,h = [1,2,3,4,5,6,7,8,9]


a = ++a
b = --b
c = c * c
d = d / d
e = e ** e
f = f % f

zmienne = [a,b,c,d,e,d,f,g,h]

for x in range(6):
    print(zmienne[x])

#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:


import math

print("\n pod pkt. 1: \n")
print(math.e**10)

print("\n pod pkt. 2: \n")

a= pow((math.log(5+((math.sin(8.00)**2)))),1/6)
print (a)

print("\n pod pkt. 3: \n")

print(math.floor(3.55))

print("\n pod pkt. 4: \n")

print(math.ceil(4.80))
#nwm czemu to nie dziala

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z
# powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)

piosenka = "Just la la la la la It goes around the world Just la la la la la It's all around the world"

print(piosenka.count("la"))

#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej
# drugą i ostatnią literę, wykorzystując indeksy.


wyraz1 = "maciej"
wyraz2 = "szulia"

i = 1

while i < len(wyraz1):
  print(i)
  i += 1

i = i-1

print(wyraz1[1] + wyraz1[i])
print(wyraz2[1] + wyraz2[i])