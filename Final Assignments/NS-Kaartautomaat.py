stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
def inlezen_beginstation(beginstation):
    while True:
        if beginstation in stations:
            return beginstation
            break
        else:
            print('{} hoort niet bij het mogelijke traject.'.format(beginstation))
            beginstation = input('Voer het beginstation in: ')

def inlezen_eindstation(beginstation, eindstation):
    while True:
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
                break
        else:
            print('{} hoort niet bij het mogelijke traject.'.format(eindstation))
            eindstation = input('Voer het eindstation in: ')

def omroepen_reis(beginstation, eindstation):
    IBeginstation = (stations.index(beginstation)) + 1
    IEindstation = (stations.index(eindstation)) + 1
    afstand = IEindstation - IBeginstation
    prijs = afstand * 5
    tussenstations = []
    for i in range(stations.index(beginstation), stations.index(eindstation)):
        tussenstations.append(stations[i])
    print('Jij stapt in de trein in: {}, het {}e station in het traject'.format(beginstation, IBeginstation))
    print('De tussenstations zijn: {}'.format(tussenstations))
    print('Jij stapt uit in: {}, het {}e station in het trajcect'.format(eindstation, IEindstation))
    print('De afstand bedraagt {} stations'.format(afstand))
    print('De prijs van de reis bedraagt €{},-'.format(prijs))


invoer1 = input('Voer het beginstation in: ')
invoer2 = input('Voer het beginstation in: ')
inlezen_beginstation(invoer1)
inlezen_eindstation(invoer1, invoer2)
omroepen_reis(invoer1, invoer2)



