def convert(temp):
    newTemp = temp * 1.8 + 32
    return str(newTemp)


invoer = eval(input('Hoeveel graden celsius is het?'))

print('Dat is {} °F'.format(convert(invoer)))
