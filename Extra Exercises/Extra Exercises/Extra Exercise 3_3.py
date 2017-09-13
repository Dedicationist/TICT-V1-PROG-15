woord = input('Welke woord wil je weten?')
e = 0
o = 0
i = 0
for letter in woord:
    if letter == 'e':
        e = e + 1
print('Het woord bevat ' + str(e) + ' keer de letter e.')

for letter in woord:
    if letter == 'o':
        o = o + 1
print('Het woord bevat ' + str(o) + ' keer de letter o.')

for letter in woord:
    if letter == 'i':
        i = i + 1
print('Het woord bevat ' + str(i) + ' keer de letter i.')

