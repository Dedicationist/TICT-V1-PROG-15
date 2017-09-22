zin = input('Geef een zin om het acroniem te generen: ')
woorden = zin.split()
acroniem = ''
for woord in woorden:
    acroniem = acroniem + woord[0]
print(acroniem)
