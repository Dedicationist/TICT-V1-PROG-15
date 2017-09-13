getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
oneven= 0
for getal in getallenrij:
    if getal%2 == 0:
        oneven = oneven + 1
print('Het aantal oneven getallen is ' + str(oneven))

deelbaar = 0
for getal in getallenrij:
    if getal%2 == 0 and getal%3 == 0:
        deelbaar = deelbaar + 1
print ('Het aantal getallen dat deelbaar is door twee en door 3 is ' + str(deelbaar))
