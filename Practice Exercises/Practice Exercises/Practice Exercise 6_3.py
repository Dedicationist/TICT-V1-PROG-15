invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lst = invoer.split('-')
lst = [int(i) for i in lst]
lst.sort()
print('De gesorteerde list van ints: {}'.format(lst))
GrootsteGetal= max(lst)
KleinsteGetal= min(lst)
AantalGetallen= len(lst)
SomGetallen= sum(lst)
GemiddeldeGetallen= SomGetallen / AantalGetallen

print('Grootste getal: {} en kleinstte getal: {}'.format(GrootsteGetal, KleinsteGetal))
print('Aantal getallen: {} en som van de getallen: {}'.format(AantalGetallen, SomGetallen))
print('Gemiddelde: {}'.format(GemiddeldeGetallen))


