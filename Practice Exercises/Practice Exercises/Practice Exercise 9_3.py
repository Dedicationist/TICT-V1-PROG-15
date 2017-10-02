import csv
lst = []
with open('PE9_3.csv','r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    for row in reader:
        hscore = max(lst)
        if row[2] > hscore:









