getallenrij = [2, 4, 5, 6, 8, 10, 9, 7]
som = 0
for getal in getallenrij:
    if getal %3 == 0:
        som = som + 1
print ('Het aantal getallen deelbaar door 3 is ' + str(som))
