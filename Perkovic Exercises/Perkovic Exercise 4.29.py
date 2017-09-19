def stats(txtbestand):
    infile = open(txtbestand)
    uitvoer = infile.readlines()

    AantalRegels = 0
    for bereken in uitvoer:
        AantalRegels = len(uitvoer)
    print('line count: {}'.format(AantalRegels))

    AantalWoorden = 0
    for bereken in uitvoer:
        woord = bereken.split()
        AantalWoorden = AantalWoorden + len(woord)
    print('word count: {}'.format(AantalWoorden))

    AantalKarakters = 0
    for bereken in uitvoer:
        AantalKarakters = AantalKarakters + len(bereken)
    print('character count: {}'.format(AantalKarakters))

    infile.close()

stats('example.txt')

