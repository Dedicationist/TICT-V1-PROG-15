def initials(first, last):
    f = first[0]
    l = last[0]
    ini = '{}.{}'.format(f, l)
    return ini

finvoer = input('Geef je voornaam: ')
linvoer = input('Geef je achternaam: ')
print(initials(finvoer, linvoer))
