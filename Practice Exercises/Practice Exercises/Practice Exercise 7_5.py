def namen(naam):
    invoer = input('Voornaam?: ')
    namenteller = {}
    while invoer is not '':
        invoer = input('Voornaam?: ')
        if invoer in namenteller.keys():
            namenteller[invoer] += 1
        elif invoer not in namenteller.keys():
            namenteller[invoer] = 1

    if invoer is '':
        namenteller.pop('')
        for namen in namenteller:
                print('{} studenten met de naam {}'.format(namenteller[namen], namen))

namen('naam')



