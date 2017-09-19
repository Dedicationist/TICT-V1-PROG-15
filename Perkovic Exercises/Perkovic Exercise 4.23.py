def gemiddelde(zin):
    ListZin = zin.split(' ')
    lst = []
    for woorden in ListZin:
        lst.append(len(woorden))
    return sum(lst) / len(lst)

NeedAverage = input('Enter a sentence: ')
average = gemiddelde(NeedAverage)
print(average)
