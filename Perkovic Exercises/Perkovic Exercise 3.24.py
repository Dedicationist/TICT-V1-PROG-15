#lst = ['cia', 'secret', 'mi6', 'isi', 'secret']
lst = eval(input('Please give an input (list): '))
for words in lst:
    if words != 'secret':
        print(words)

