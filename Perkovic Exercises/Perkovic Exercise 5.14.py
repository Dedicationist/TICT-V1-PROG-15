def mult3(list):
    for numbers in list:
        if numbers % 3 == 0:
            print(numbers)

invoer = eval(input('Put in a list of integers: '))
mult3(invoer)
