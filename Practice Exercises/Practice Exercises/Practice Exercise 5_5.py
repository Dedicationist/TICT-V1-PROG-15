def gemiddelde(zin):
    ListZin = zin.split(' ')
    lst = []
    for woorden in ListZin:
        lst.append(len(woorden))
    return sum(lst) / len(lst)

zinvoer = input('Type een zin om de gemiddelde lengte van de woorden te berekenen')
print('De gemiddelde lengte van de woorden in je zin is {}'.format(gemiddelde(zinvoer)))
