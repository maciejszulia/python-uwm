# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

#MACIEJ SZULIA 154733

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