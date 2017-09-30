def hexASCII():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for karakters in alphabet:
        ASCKarakters = str(hex(ord(karakters)))
        ASCKarakters = ASCKarakters.strip('0x')
        print('{}:{}'.format(karakters, ASCKarakters))


hexASCII()
