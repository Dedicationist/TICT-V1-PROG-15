def test(number):
    if number < 0:
        return 'Negative'
    elif number == 0:
        return 'Zero'
    else:
        return 'Positive'

invoer = eval(input('Put in a number to test it: '))
print(test(invoer))
