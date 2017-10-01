stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = ''
eindstation = ''
def inlezen_beginstation(beginstation):
    while beginstation not in stations:
        beginstation = input('Voer het beginstation in: ')
        print('{} hoort niet bij het traject')
    if beginstation in stations:
        return beginstation


