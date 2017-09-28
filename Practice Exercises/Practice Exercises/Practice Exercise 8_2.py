import random
def monopolyworp():
    dobbel1 = random.randrange(1, 7)
    dobbel2 = random.randrange(1, 7)
    somOgen = dobbel1 + dobbel2
    dubbelSom= 0
    if dobbel1 == dobbel2:
        print('{} + {} = {}(dubbel)'.format(dobbel1, dobbel2, somOgen))
    else:
        print('{} + {} = {}'.format(dobbel1, dobbel2, somOgen))

    while dobbel1 == dobbel2:
        dobbel1 = random.randrange(1, 7)
        dobbel2 = random.randrange(1, 7)
        somOgen = dobbel1 + dobbel2
        if dobbel1 == dobbel2:
            print('{} + {} = {}(dubbel)'.format(dobbel1, dobbel2, somOgen))
        else:
            print('{} + {} = {}'.format(dobbel1, dobbel2, somOgen))
        dubbelSom += 1

        if dubbelSom == 3:
            break
            dobbel1 = random.randrange(1, 7)
            dobbel2 = random.randrange(1, 7)
            somOgen = dobbel1 + dobbel2
            print('{} + {} = (direct naar de gevangenis)'.format(dobbel1, dobbel2))



monopolyworp()

