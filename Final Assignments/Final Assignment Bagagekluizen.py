def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    AantalKluizen = infile.readlines()
    VrijeKluizen = 0
    for regels in AantalKluizen:
        VrijeKluizen = VrijeKluizen + 1
    infile.close()

def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    infile = open('kluizen.txt','r+')
    IngelezenNummers = infile.read()
    for nummers in kluisnummers:
        if nummers in IngelezenNummers:
            kluisnummers.pop(nummers)

    if kluisnummers == []:
        print('Er zijn geen kluizen meer beschikbaar')
    else:
        ToegewezenKluis= kluisnummers[0]
        Code = eval(input('Geef een code van vier cijfers: '))
        outfile = infile.write('Code = {}, kluisnummer = "{}'.format(Code, ToegewezenKluis))
        print('Uw kluisnummer is: {}'.format(ToegewezenKluis))
