def easyCrypto(string):
    encrypted = ''
    for i in string:
        if ord(i) % 2 == 1:
            i = chr(ord(i) + 1)
        else:
            i = chr(ord(i) - 1)
        encrypted += i
    return encrypted

invoer = input('Voer een woord in: ')
print(easyCrypto(invoer))


