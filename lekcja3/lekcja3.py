# MACIEJ SZULIA 154733
# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x ∈ B i x jest liczbą podzielną przez 2}

A = [1 - x for x in range(10)]
print(A)

B = [4 ** y for y in range(8)]
print(B)

C = [B[i] for i in range(len(B)) if B[i] % 2 == 0]
print(C)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1,
# następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy

import random

lista1 = []
for i in range(10):
    lista1.append(random.randrange(1, 100))
print(lista1)

parzyste = [lista1[i] for i in range(len(lista1)) if lista1[i] % 2 == 0]
print(parzyste)


# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje
# (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy,
# gdzie będą produkty, których wartość to sztuki.

produkty = {'produkt': 'jajka', 'jednostka': 'sztuki',
'produkt': 'jabłka', 'jednostka': 'kilogram',
'produkt': 'mrożonki', 'jednostka': 'sztuki',
'produkt': 'ser', 'jednostka': 'plasterki'
            }

produkty_sztuki = []

print(produkty_sztuki)

# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

def trojkat(a, b, c):
    if a ** 2 & b ** 2 == c ** 2:
        print("jest prostokątny")
    else:
        print("nie jest prostokątny")


trojkat(1, 1, 1)
trojkat(1, 2, 1)


# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

def pole_trapez(a=1, b=2, h=5):
    return ((a + b) * h) / 2


print(pole_trapez())
print(pole_trapez(20, 20, 20))


# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

def iloczyn_ciagu(a=1, b=4, ile=10):
    wynik = [a]
    for ile in range(ile):
        wynik.append(wynik[ile]*b)
    return wynik

print(iloczyn_ciagu(1, 4, 10))

# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.

# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci:
# klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.

# Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.
