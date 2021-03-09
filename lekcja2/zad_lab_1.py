#Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz
# po dwie zmienne każdego typu a następnie wyświetl te zmienne

#MACIEJ SZULIA 154733

print("zadanie1: \n")

a = 10
aa = 20
b = 20.1
bb = 20.2
c = 'string'
cc = 'string2'
d = (3+1j)
dd = (3+2j)

zmienne = [a,aa,b,bb,c,cc,d,dd]

for x in range(8):
    print(zmienne[x])
    
for x in range(8):
    print(type(zmienne[x]))