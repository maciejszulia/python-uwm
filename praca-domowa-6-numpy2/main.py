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

macierz_a1 = np.arange(1,10,1).reshape(1,3)
macierz_b1 = np.arange(1,2,0.1).reshape(1,3)

