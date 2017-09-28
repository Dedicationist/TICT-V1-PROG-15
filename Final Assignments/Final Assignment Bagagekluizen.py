def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    AantalKluizen = infile.readlines()
    VrijeKluizen = 0
    for regels in AantalKluizen:
        VrijeKluizen = VrijeKluizen + 1
    print('Er is/zijn nog {} kluis/kluizen vrij.'.format(VrijeKluizen))
    infile.close()

def nieuwe_kluis():
    kluisnummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    infile = open('kluizen.txt','r+')
    IngelezenNummers = infile.readlines()
    for nummers in kluisnummers:
        if nummers in IngelezenNummers:
            kluisnummers.remove(nummers)

    if kluisnummers == []:
        print('Er zijn geen kluizen meer beschikbaar')
    else:
        ToegewezenKluis= kluisnummers[0]
        Code = input('Geef een code van vier cijfers: ')
        if len(Code) < 4:
            print('Die code is langer dan 4 tekens, voer een nieuwe code in')
            Code = eval(input('Geef een code van vier cijfers: '))
        outfile = infile.write('{};{}\n'.format(ToegewezenKluis, Code))
        print('Uw kluisnummer is: {}'.format(ToegewezenKluis))
    infile.close()

def kluis_openen():
    nummer= eval(input('Geef het nummer: '))
    code = input('Geef je code: ')
    CodeNummer= '{};{}\n'.format(nummer, code)
    infile = open('kluizen.txt','r')
    Combinatie = infile.readlines()
    for combo in Combinatie:
        if combo in CodeNummer:
            print('Dit is een correcte combinatie')
            break
        else:
            print('Dit is geen correcte combinatie van een kluisnummmer en de bijbehorende code')
    infile.close()

while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik wil stoppen')
    invoer = eval(input('Wat is uw keuze? (1, 2, 3 of 4)'))
    if invoer == 1:
        toon_aantal_kluizen_vrij()
    elif invoer == 2:
        nieuwe_kluis()
    elif invoer == 3:
        kluis_openen()
    else:
        break


