def different(lst):
    som = 0
    for lsts in lst:
        for number in lsts:
            if number not in lsts:
                som+= 1
    print(som)


t = [[1,0,1],[0,1,0]]
different(t)
