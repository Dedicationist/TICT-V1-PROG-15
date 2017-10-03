def inValues(invoer):
    errorcounter = 0
    if errorcounter >= 2:
        print('Two errors in a row. Quitting...')
    try:
        invoer = int(input('Please enter a number: '))
    except ValueError:
        invoer = int(input('Please enter a number: '))
        errorcounter += 1
    except TypeError:
        invoer = int(input('Please enter a number: '))
        errorcounter += 1
    except NameError:
        invoer = int(input('Please enter a number: '))
    except ZeroDivisionError:
        return
invoer = int(input('Please enter a number: '))

inValues(invoer)
