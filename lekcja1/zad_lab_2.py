# Zad2. Stwórz skrypt kalkulator,
# w którym wykorzystać wszystkie podstawowe działania arytmetyczne

#MACIEJ SZULIA 154733

a = 10
aa = 20
b = 20.1
bb = 20.2
c = 'string'
cc = 'string2'
d = (3+1j)
dd = (3+2j)


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