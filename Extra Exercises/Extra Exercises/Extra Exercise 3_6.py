getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
maximum = 0
minimum = 0
for getal in getallenrij:
    if getal == max(getallenrij):
       maximum = maximum + getal
    if getal == min(getallenrij):
        minimum = minimum + getal
print('Het kleinste getal is ' + str(minimum))
print('Het grootste getal is ' + str(maximum))
