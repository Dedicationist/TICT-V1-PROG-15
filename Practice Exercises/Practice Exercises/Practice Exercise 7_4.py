def ticker(tickersymbols):
    infile= open('tickersymbols.txt', 'r')
    ticker = {}
    inhoud = infile.readlines()
    for regel in inhoud:
        info = regel.split(':')
        info[1] = info[1].strip()
        ticker[info[1]]= info[0]
    return ticker

tickerfunctie = ticker('tickersymbols.txt')

invoer2 = input('Enter ticker sym: ')
print('Company name: {}'.format(tickerfunctie[invoer2]))

invoer = input('Enter a Company name: ')
for invoer2 in tickerfunctie:
    if tickerfunctie[invoer2] == invoer:
        print('Ticker symbol=', invoer2)

