infile = open('kaartnummers.txt', 'r')
uitvoer = infile.readlines()
infile.close()

for regel in uitvoer:
    uitvoer1 = regel.split(',')
    print('{} heeft kaartnummer: {}'.format(uitvoer1[1].strip(), uitvoer1[0]))
