def pairSum(lst, n):
    for numbers in lst:
        if n - numbers in lst:
            print('{} {}'.format(lst.index(numbers), lst.index(n-numbers)))

pairSum([7, 8, 5, 3, 4, 6], 11)
