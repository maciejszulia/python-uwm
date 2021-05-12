# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

import numpy as np

macierz_a = np.arange(0, 3)
macierz_b = np.arange(1, 4)
print(macierz_a, macierz_b)
print(macierz_a * macierz_b)

# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

x = np.arange(1, 10).reshape(3, 3)
print(x)
print("najmniejszy wiersz: ", np.amin(x, axis=0), ", najmniejsza kolumna: ", np.amin(x, axis=1))

y = np.arange(1, 17).reshape(4, 4)
print(y)
print("najmniejszy wiersz: ", np.amin(y, axis=0), ", najmniejsza kolumna: ", np.amin(y, axis=1))

# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

print(np.dot(macierz_a, macierz_b))  # nie jestem pewien czy to jest to

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite,
# a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

import math

macierz_a1 = np.full((1, 3), 5)
macierz_b1 = np.full((1, 3), math.pi)

print(macierz_a1, macierz_b1)
print(macierz_a1 * macierz_b1)

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości
# a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

macierz_a2 = np.arange(6).reshape(2, 3)
print(macierz_a2)
a = [np.sin(i) for i in macierz_a2]
print(a)

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości
# a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.

macierz_b2 = np.arange(6).reshape(2, 3)
b = [np.cos(i) for i in macierz_b2]
print(b)

# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

macierz_dodawanie = np.add(a, b)
print(macierz_dodawanie)

# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

macierz_3 = np.arange(9).reshape(3, 3)
print(macierz_3)
for i in macierz_3:
    print(i)

# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element
# korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())

macierz_4 = np.arange(9).reshape(3, 3).flat  # to jest to? nie wiem....
for i in macierz_4:
    print(i)

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

macierz_5 = np.ndarray(shape=(9,9),dtype=int)
macierz_5.fill(9)
print(macierz_5)
macierz_5 = macierz_5.reshape(3,27)
print(macierz_5)                #ilość wymiarów które można stworzyć z tej macierzy to dzielnik liczby 81


# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

wektor = np.arange(12).reshape(3,4)
wektor_2 = np.arange(12).reshape(4,3)
wektor_3 = np.arange(12).reshape(2,6)

print(wektor)
print(wektor_2)
print(wektor_3)

print(wektor.flatten())
print(wektor_2.flatten())
print(wektor_3.flatten())       #som identyczne hehe