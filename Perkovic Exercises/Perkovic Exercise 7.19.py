def inValues(invoer):
    errorcounter = 0
    if errorcounter >= 2:
        print('Two errors in a row. Quitting...')
    try:
        invoer = input('Please enter a number: ')
    except ValueError:
        invoer = input('Please enter a number: ')
        errorcounter += 1
    except TypeError:
        invoer = input('Please enter a number: ')
        errorcounter += 1
invoer = input('Please enter a number: ')
while True:
    inValues(invoer)
