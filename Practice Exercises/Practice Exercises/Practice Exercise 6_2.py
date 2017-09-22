zin = eval(input('Geef een lijst van minimaal 10 strings: '))
lst = []
for woord in zin:
    if len(zin) > 10:
        print('Je lijst is te kort...')
    else:
        if len(woord) == 4:
            lst.append(woord)

print('De nieuwe-gemaakte lijst met alle vier-letter strings is: {}'.format(lst))

