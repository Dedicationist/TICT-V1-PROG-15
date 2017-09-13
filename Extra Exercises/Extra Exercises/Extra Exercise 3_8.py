getallenrij = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


getal1 = False
getal2 = False

invoer1 = eval(input('Voer het eerste getal in:'))
invoer2 = eval(input('Voer het tweede getal in:'))

for getal in getallenrij:
    if invoer1 == getal:
        getal1 = True
    if invoer2 == getal:
        getal2 = True

if getal1 and getal2:
    print ('Beide getallen komen voor in de getallenrij')
if getal1 and not getal2:
    print ('Een van de getallen komt voor in de getallenrij')
if getal2 and not getal1:
    print ('Een van de getallen komt voor in de getallenrij')
if not getal1 and not getal2:
    print('Geen van beide getallen komt voor in de getallenrij')
