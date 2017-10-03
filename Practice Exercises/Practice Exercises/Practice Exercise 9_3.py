import csv
lst = []
lstnaam = []
lstdatum = []
with open('PE9_3.csv','r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        lst.append(row[2])
        lstnaam.append(row[0])
        lstdatum.append(row[1])
    hscore = max(lst)
    indexhscore = lst.index(hscore)
    print('De hoogste score is: {} op {} behaald door {}'.format(hscore, lstnaam[indexhscore], lstdatum[indexhscore]))





