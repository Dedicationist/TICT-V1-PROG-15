import datetime
import csv

with open('PE9_2.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('datum ingelogd', 'voorletter(s)', 'naam', 'geboortedatum', 'email-adres'))
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        else:
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")
            datum1 = datetime.datetime.today()
            datum = datum1.strftime('%a %d %b %Y %X')
            writer.writerow((datum, voorl, naam, gbdatum, email))
