def standaardtarief(afstandKM):
    if afstandKM < 0:
        prijs = 0
        return prijs
    else:

     if afstandKM >= 50:
        prijs = 0.6 * afstandKM + 15
     if afstandKM <= 50:
        prijs = 0.8 * afstandKM
        return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'Ja' or weekendrit == 'ja':
        weekendrit = True
    if weekendrit == 'Nee' or weekendrit =='nee':
        weekendrit = False
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        eindbedrag = standaardtarief(afstandKM) * 0.7
    if leeftijd >= 12 and leeftijd < 65 and weekendrit == False:
        eindbedrag = standaardtarief(afstandKM)
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        eindbedrag = standaardtarief(afstandKM) * 0.65
    if leeftijd >= 12 and leeftijd < 65 and weekendrit == True:
        eindbedrag = standaardtarief(afstandKM) * 0.60
    return str(eindbedrag)

afstandKM = eval(input('Hoeveel km is uw reis?'))
leeftijd = eval(input('Hoe oud bent u?'))
weekendrit = input('Reist u in het weekend?')

print ('Dan is de prijs van uw reis: €' + ritprijs(leeftijd, weekendrit, afstandKM) + ' Fijne reis!')
# Getest, werkend en nagerekent met afstandKM = 24, leeftijd = 11, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 54, leeftijd = 12, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 49, leeftijd = 64, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 102, leeftijd = 68, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 33, leeftijd = 65, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 234, leeftijd = 18, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 102, leeftijd = 66, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 12345, leeftijd = 97, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 3.3, leeftijd = 17, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 1, leeftijd = 1, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 0, leeftijd = 17, weekendrit = nee
# Getest, werkend en nagerekent met afstandKM = 0, leeftijd = 18, weekendrit = ja
# Getest, werkend en nagerekent met afstandKM = 51, leeftijd = 32, weekendrit = nee
