def seizoen(maand):
    if maand >= 3 and maand <= 5:
        return('Het is lente')
    elif maand >= 6 and maand <= 8:
        return('Het is zomer')
    elif maand >= 9 and maand <= 11:
        return('Het is herfst')
    elif maand >= 12 and maand <= 2:
        return('Het is winter')
maandnummer= eval(input('Welk maandnummer is het?'))
print(seizoen(maandnummer))
