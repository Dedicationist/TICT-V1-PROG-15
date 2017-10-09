som = []
while True:
    getal = eval(input('Geef een getal: '))
    som.append(getal)
    if getal == 0:
        som.pop(getal)
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(som), sum(som)))
        break
