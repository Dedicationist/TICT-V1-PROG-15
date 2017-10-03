try:
    aantal = int(input('Hoeveel mensen gaan er mee op reis? '))
    if aantal < 0:
        print('Negatieve getallen zijn niet toegestaan')
    else:
        print('Dan zijn de kosten per persoon: {} euro.'.format(4356 / aantal))
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik CIJFERS voor het invoeren van het aantal')
