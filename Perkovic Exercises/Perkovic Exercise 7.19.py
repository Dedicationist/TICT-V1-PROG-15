def inValues(invoer):
    som = 0
    errorcounter = 0
    errormessage = 'Error. Please re-enter the value'
    quit = 'Error. Two errors in a row. Quitting...'
    while True:
        try:
            if invoer == 0:
                print(som)

            invoer = eval(input('Please enter a number: '))
            som += invoer
        except ValueError:
            errorcounter += 1
            if errorcounter >= 2:
                print(quit)
                break
            else:
                print(errormessage)
                invoer = eval(input('Please enter a number: '))
        except TypeError:
            errorcounter += 1
            if errorcounter >= 2:
                print(quit)
                break
            else:
                print(errormessage)
                invoer = eval(input('Please enter a number: '))
        except NameError:
            errorcounter += 1
            if errorcounter >= 2:
                print(quit)
                break
            else:
                print(errormessage)
                invoer = eval(input('Please enter a number: '))
        except IndexError:
            errorcounter += 1
            if errorcounter >= 2:
                print(quit)
                break
            else:
                print(errormessage)
                invoer = eval(input('Please enter a number: '))


invoer = eval(input('Please enter a number: '))
inValues(invoer)
