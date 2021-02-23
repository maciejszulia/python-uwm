#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej
# drugą i ostatnią literę, wykorzystując indeksy.

#MACIEJ SZULIA 154733

wyraz1 = "maciej"
wyraz2 = "szulia"

i = 1

while i < len(wyraz1):
  print(i)
  i += 1

i = i-1

print(wyraz1[1] + wyraz1[i])
print(wyraz2[1] + wyraz2[i])