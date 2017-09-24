def indexes(string, letter):
    lst= []
    for i in range(0, len(string)):
        if string[i] == letter:
            lst.append(i)
    return lst

string = input('Voer een woord in: ')
letter = input('Voer een letter in: ')
uitvoer = indexes(string, letter)
print(uitvoer)
