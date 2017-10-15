def doubles(lst):
    for numbers in lst:
        if numbers * 2 == lst[lst.index(numbers) + 1]:
            print(lst[lst.index(numbers) + 1])

#invoer = eval(input('Put in a list of integers to check for doubles: '))
doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5])

#[3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]

