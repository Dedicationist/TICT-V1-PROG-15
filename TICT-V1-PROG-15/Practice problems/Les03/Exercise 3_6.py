getallenrij = [2, 4, 5, 8, 10, 9, 7]
zoekgetal = eval (input('Welk getal wil je zoeken?'))
gevonden = False
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True

if gevonden == True:
    print ('Het zoekgetal zit in de getallenrij.')
else:
    print ('Het zoekgetal zit niet in de getallenrij.')
