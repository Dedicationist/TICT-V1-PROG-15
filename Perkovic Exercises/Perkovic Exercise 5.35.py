def pixels(lst):
    PosPixels = 0
    for nummers in lst:
        for nummers2 in nummers:
            if nummers2 > 0:
                PosPixels = PosPixels + 1
    return PosPixels

invoer = eval(input('Geef een twee dimensionale lijst: '))
print(pixels(invoer))


#[[0, 156, 0, 0],[34, 0, 0, 0],[23, 123, 0, 34]]
