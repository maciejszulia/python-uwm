import sys as system
import math

#Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
#a następnie odwróć całą listę. Po odwróceniu listy dodaj kilka pozycji
#(dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać 10 pozycji)


lista_filmow = [
    "Borat: Podpatrzone w Ameryce, aby Kazachstan rósł w siłę, a ludzie żyli dostatniej (2001)",
    "The Shawshank Redemption (1994)",
    "Intouchables (2011)",
    "The Godfather (1972)",
    "12 Angry Men (1957)"
]

nr = 1
print("lista filmów: ")
for i in lista_filmow:
    print(nr, i)
    nr = nr + 1


print("\nodwrócona lista filmów: ")
nr = 1
for i in reversed(lista_filmow):
    print(nr, i)
    nr = nr + 1

lista_filmow2 = [
    "One Flew Over the Cuckoo's Nest (1975)",
    "The Godfather: Part II (1974)",
    "Schindler's List (1993)",
    "Pulp Fiction (1994)",
    "Se7en (1995)"
]

print("\ndodaj 5 tytułów: ")

for i in range(5):
    lista_filmow.append(lista_filmow2[i])

nr = 1
for i in lista_filmow:
    print(nr, i)
    nr = nr + 1


#Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1.
#Pomyśl co może być kluczem

slownik_filmow = {'tytul': lista_filmow}

slownik_filmow.items()


#Zad 3. Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów
#z obecnego semestru oraz ich skrótami. Policz liczbę elementów w słownik

lista_przedmiotow = [
    "CAD komputerowe wspomaganie programowania",
    "Wizualizacja danych",
    "Rachunek różn. i całkowy",
    "Przedmiot humanizujacy",
    "Jezyk obcy",
    "Elementy matematyki dyskretnej",
    "Programowanie strukturalne",
]
lista_przedmiotow_skroty = [
    "CAD", "Wiz. danych", "Rach. różn. i całk.", "Human", "J. obcy", "El. mat. dyskret.", "Prog. strukt."
]

slownik_przedmiotow = {'przedmiot': lista_przedmiotow, 'skrócone nazwy': lista_przedmiotow_skroty}


#Zad 4. Napisz skrypt gdzie wczytasz liczbę dowolnego typu
# i podnieś ją do tej samej potęgi. Użyj funkcji input.

val = input("wprowadz liczbe:\n")
val = float(val)

print(f'{val}^2 = {val ** 2}')

#Zad 5. Napisz skrypt gdzie wczytasz dowolny ciąg znaków,
# i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).



system.stdout.write("Wpisz ciąg znaków: ")
ciag_znakow = system.stdin.readline()
print(ciag_znakow.count("a"))

#Zad 6. Wczytaj trzy liczby całkowite a,b,c
# i sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c

print("Wczytaj trzy liczby całkowite a,b,c: \n")

a = input("a = ")
a = int(a)

b = input("b = ")
b = int(b)

c = input("c = ")
c = int(c)

if a % 2 == 0 and b > c:
    print("prawda")
else:
    print("false")

#Zad 7. Napisz skrypt, gdzie stworzysz listę składającą
# się z liczb typu int i float. Następnie za pomocą pętli for
# oblicz sumę elementu obecnego z poprzednim.

lista = [1, 2.2, 3, 4.4, 5, 6.6]

i = 0
for i in range(len(lista)-1):
    suma = lista[i] + lista[i+1]
    print(suma)

#Zad 8. Napisz skrypt, który
# za pomocą pętli while pobiera 10 liczb,
# a następnie dodaje do listy tylko liczby całkowite

lista = []
i = 0
while i < 10:
    a = input()
    a = int(a)
    lista.append(a)
    i += 1
print(lista)

#Zad 9. Napisz skrypt, który rysuje następującą literę: 0

lista = [1,2,3,4,5,6]

i = 1
for i in range(6):
   if lista[i] % 5 == 1:
       print("000000")
   if lista[i] % 5 != 1:
       print("0    0")

#Zad 10. Napisz skrypt, w którym użytkownik ma podać liczbę
# i który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.