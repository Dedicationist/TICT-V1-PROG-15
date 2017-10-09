invoer = input('Geef een woord van vier letters: ')
while True:
    if len(invoer) is not 4:
        print('Dat woord heeft geen vier letters... Het heeft {} letters'.format(len(invoer)))
        invoer = input('Geef een woord van vier letters: ')
    else:
        print('De string {} is een correcte input :)'.format(invoer))
        break
