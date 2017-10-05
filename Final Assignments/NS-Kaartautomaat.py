def inlezen_beginstation(stations):
    while True:
        beginstation = input('Voer het beginstation in: ')
        if beginstation in stations:
            return beginstation
            break
        else:
            print('{} hoort niet bij het mogelijke traject.'.format(beginstation))

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Voer het eindstation in: ')
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                return eindstation
                break
        else:
            print('{} hoort niet bij het mogelijke traject.'.format(eindstation))

def omroepen_reis(stations, beginstation, eindstation):
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

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)



