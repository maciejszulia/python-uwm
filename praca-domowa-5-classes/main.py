# Zad1
# Klasa: Material
# Atrybuty:
# rodzaj,
# długość
# szerokość
# Metody:
# konstruktor
# wyświetl_nazwę


class material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return "material: {} {}cm x {}cm".format(self.rodzaj, self.dlugosc, self.szerokosc)


# Klasa: Ubrania
# Atrybuty:
# rozmiar
# kolor
# dla_kogo
# Metody:
# wyświetl_dane – do wyświetlania informacji o ubraniu

class ubrania(material):
    def __init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return "ubranie typu {} {} {} {} {} {}".format(self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj,
                                                       self.dlugosc, self.szerokosc)


# klasa: Sweter
# Atrybuty:
# rodzaj_swetra – np.Rozpinany, z golfem itd.
# Metody:
# wyświetl_dane

class sweter(ubrania):
    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        ubrania.__init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return "sweterek typu: {}, {}, {}, {}, {}, {}, {}".format(self.rodzaj_swetra, self.rozmiar, self.kolor,
                                                                  self.dla_kogo,
                                                                  self.rodzaj,
                                                                  self.dlugosc, self.szerokosc)


material_1 = material("bawelna", 10, 10)
print(material_1.wyswietl_nazwe())

bluza_1 = ubrania("L", "czarny", "kobieta", "bawelna", 10, 10)
print(bluza_1.wyswietl_dane())

sweterek_1 = sweter("golf4", "XXXL", "tecza", "nonbinary", "rzygi_konia", "20 km", "20 km")
print(sweterek_1.wyswietl_dane())


# zad 2
# Przeciąż metodę ``__add__()`` dla klasy Kwadrat,
# która będzie zwracała instancje klasy Kwadrat o nowym boku,
# będącym sumą długości boku kwadratu oraz obwodu kwadratu      #?????

# class kwadrat:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):

