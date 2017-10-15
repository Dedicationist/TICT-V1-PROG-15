def intersect(lst1, lst2):
    lst = []
    for numbers in lst1:
        if numbers in lst2:
            lst.append(numbers)
    print(lst)

intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9])

