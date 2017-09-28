def namen(naam):
    invoer = input('Voornaam?: ')
    namenteller = {}
    while invoer is not '':
        invoer = input('Voornaam?: ')
        if invoer in namenteller.keys():
            namenteller[invoer] += 1
        else:
            namenteller[invoer] = 1

    if invoer is '':
        namenteller.pop('')
        for namen in namenteller:
                print('{} student(en) met de naam {}'.format(namenteller[namen], namen))

namen('naam')



