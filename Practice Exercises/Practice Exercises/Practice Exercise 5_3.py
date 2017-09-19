infile = open('kaartnummers.txt', 'r')
uitvoer = infile.readlines()
infile.close()
AantalRegels = 0
MaxKaartnummer = max(uitvoer).split(',')

for regel in uitvoer:
    AantalRegels = AantalRegels + 1
print('Deze file telt {} regels'.format(AantalRegels))

print('Het grootste kaartnummer is: {}'.format(MaxKaartnummer[0].strip()))
