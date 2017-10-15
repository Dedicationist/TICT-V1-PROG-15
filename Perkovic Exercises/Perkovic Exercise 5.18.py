def four_letter(lst):
    lst2 = []
    for words in lst:
        if len(words) == 4:
            lst2.append(words)
    return lst2
print(four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust']))

