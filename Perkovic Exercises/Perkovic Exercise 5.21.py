def pair(lst1, lst2, n):
    for numbers in lst1:
        if n - numbers in lst2:
            print('{} {}'.format(numbers, n - numbers))

pair([8, 10, 6, 9], [8, 7, 9, 12], 18)
