import numpy as np

# Zad1.
# Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.

wielokrotności = np.arange(start=0, stop=3 * 15, step=3, dtype=int)
print(wielokrotności)

# Zad2.
# Stwórz listę składającą się z wartości zmiennoprzecinkowych
# a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64

zmiennoprzecinkowe = np.arange(start=0, stop=10, step=1.1, dtype=float)
print(zmiennoprzecinkowe)

przekonwertowana = zmiennoprzecinkowe.astype('int64')
print(przekonwertowana)


# Zad3.
# Napisz funkcję, która będzie:
# Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
#
# def funkcja1():
#     return np.ndarray(n*n)

# Zad4.
#
# Napisz funkcję, która będzie przyjmowała 2 parametry:
# liczbę, która będzie podstawą operacji potęgowania
# oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową
# kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]

def funkcja_zad4(podstawa, ilość_kolejnych):
    return np.logspace(start=1, stop=ilość_kolejnych, base=podstawa, num=ilość_kolejnych, dtype="int64")


print(funkcja_zad4(2, 4))
print(funkcja_zad4(20,20))



# print(type(funkcja_zad4(2,4)))

# Zad5.
# Napisz funkcję, która:
# Na wejściu przyjmuje jeden parametr określający długość wektora
# Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# Generuj macierz diagonalną z w/w wektorem jako przekątną

def funkcja_zad5(dl_wektora):
    wektor = np.arange(dl_wektora)
    wektor = np.flip(wektor)
    return np.diag(wektor)


print(funkcja_zad5(10))

# # Zad6.
# # Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa)
# # w postaci wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# # Jedno z tych słów powinno być wypisane od prawej do lewej.
#
# def wykreslanka(slowo_1, slowo_2, slowo_3): #slowo1 - wiersz slowo2 - kolumnaslowo 3- ukos
#     wymiar = len(slowo_1) * len(slowo_2)
#     wynik = np.ndarray(shape=wymiar, dtype=str)
#     return wynik
# print(wykreslanka("abc","bcd","cda"))


# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5,
# która będzie zawierała kolejne wartości ciągu Fibonacciego.

def zadanie_9(n=5, m=5):
    temp = [0, 1]

    for i in range(n * m - 2):
        temp.append(sum(temp[-2:]))

    return np.array(temp).reshape((n, m))


print(zadanie_9(5, 5))
