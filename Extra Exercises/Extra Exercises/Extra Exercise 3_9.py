getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
oneven = 0
som1 = 0
even = 0
som2 = 0

for getal in getallenrij:
    if not(getal%2 == 0):
        oneven = oneven + 1
        som1 = som1 + getal
print('Het aantal oneven getallen is ' + str(oneven) + ' en de som bedraagt ' + str(som1))

for getal in getallenrij:
    if (getal%2 ==0):
        even = even + 1
        som2 = som2 + getal
print('Het aan even getallen is ' + str(even) + ' en de som bedraagt ' +str(som2))
