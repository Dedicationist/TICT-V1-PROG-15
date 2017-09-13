getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]
oneven = []
even = []
minimum = 0
maximum = 0

for getal in getallenrij:
    if not(getal%2 == 0):
        oneven.append(getal)
        minimum = min(oneven)
for getal in getallenrij:
    if getal%2 == 0:
        even.append(getal)
        maximum = max(even)

print('Het minimum van de oneven getallen is ' + str(minimum))
print('Het maximum van de even getallen is ' + str(maximum))



