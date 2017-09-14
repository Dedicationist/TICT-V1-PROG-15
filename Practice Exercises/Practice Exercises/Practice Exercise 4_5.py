lst= [4, 5, 3, -81]
def kwadraten_som(grondgetallen):
    som = 0
    for getallen in lst:
            if getallen > 0:
                som = getallen**2 + som
    return(som)

print(kwadraten_som(lst))
