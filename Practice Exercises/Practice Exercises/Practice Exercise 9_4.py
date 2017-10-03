import csv
with open('PE9_4.csv', 'r+', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
    reader = csv.reader(myCSVFile, delimiter=';')
    while True:
        artikelnummer = input("Wat is het artikelnummer: ")
        if artikelnummer == 'stop':
            break
        else:
            artcode = input("Wat is de artikelcode: ")
            naam = input("Wat is de naam: ")
            voorraad = eval(input("Wat is de voorraad"))
            prijs = input('Wat is de prijs: ')
            writer.writerow((artikelnummer, artcode, naam, int(voorraad), prijs))
    voorraadcounter = 0
    lstprijs= []
    lstnaam = []
    lstvoorraad = []
    lstnummer = []
    for row in reader:
        voorraadcounter += row[3]
        lstprijs.append(row[4])
        lstnaam.append(row[2])
        lstvoorraad.append(row[3])
        lstnummer.append(row[0])
    duurste = max(lstprijs)
    iduurste = lstprijs.index(duurste)
    print('Het duurste artikel is {} en die kost €{}\n Er zijn slechts {} exemplaren in voorraad van het product met nummer {}\n In totaal hebben wij {} producten in ons magazijn liggen.'.format(lstnaam[iduurste], duurste, lstvoorraad[iduurste], lstnummer[iduurste], voorraadcounter))

