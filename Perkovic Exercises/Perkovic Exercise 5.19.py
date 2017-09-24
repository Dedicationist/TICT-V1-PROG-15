lijst1 = [1, 2, 3, 4, 5]
lijst2 = [1, 2, 3, 4, 5]

def inBoth(lst1, lst2):
    Beide = False
    for i1 in range(0, len(lst1)):
        for i2 in range(0, len(lst2)):
            if lst1[i1] == lst2[i2]:
                Beide = True
    return Beide

print(inBoth(lijst1, lijst2))


#[1, 2, 3, 4, 5]
#[6, 7, 8, 9, 10]

