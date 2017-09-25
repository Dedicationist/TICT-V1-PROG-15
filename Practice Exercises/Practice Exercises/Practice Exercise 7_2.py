invoer = ''
while len(invoer) is not 4:
    invoer = input('Geef een woord van vier letters: ')
    if len(invoer) is not 4:
        print('Dat woord heeft geen vier letters...')
