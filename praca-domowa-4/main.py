# Zad. 1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

import random

filepath = 'zadanie.txt'
f = open(filepath, "w")

for i in range(20):
    x = random.randrange(4, 9999, 4)
    f.write(str(x) + " ")

f.close()

# Zad. 2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość

f = open(filepath, "r")
print(f.readline())

f.close()

# Zad. 3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open('zadanie.txt', 'w') as writer, open('zadanie.txt', 'r') as reader:
    reader.read()
    for i in range(10):
        writer.writelines("aaaa \n")


f = open(filepath, "r")
f.read()


# Zad.4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# • nazwa_produktu, ilosc, jednostka_miary, cena_jed
# • oraz metody:
# • konstruktor – który nadaje wartości
# • wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# • ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# • ile_kosztuje() – oblicza ile kosztuje dana ilość produktu
# np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2


class NaZakupy:
    #nazwa_produktu = "zieminak"
    # ilosc = 5
    # jednostka_miary = "kg"
    #cena_jed = 2.49
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)
zakupy = NaZakupy("ziemiank", 5, "kg", 2.49)
zakupy.wyswietl_produkt()
zakupy.ile_produktu()
zakupy.ile_kosztuje()



# Zad.5
# Utwórz klasę, która definiuje ciągi arytmetyczne.
# Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# • wyświetl_dane – drukuje elementy na ekran
# • pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# • pobierz_parametry – pobiera pierwsza wartość i
#  różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# • policz_sume – liczy sume elementow
# • policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

# Zad. 6
# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka.
# Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
# • konstruktor – który nadaje wartość dla x, y i krok
# • idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
#  Stwórz instancję klasy i sprawdź jak działają wszystkie metody
