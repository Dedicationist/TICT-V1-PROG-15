def code(invoerstring):
    lst = []
    for karakters in invoerstring:
        ASCKarakter = chr(ord(karakters) + 3)
        lst.append(ASCKarakter)
    print(''.join(lst))

invoer = input('Voer een string in om deze te converteren naar ASCII: ')
code(invoer)
