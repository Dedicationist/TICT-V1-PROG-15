def reverse(string):
    a = string[2]
    b = string[1]
    c = string[0]
    print(a + b + c + '!')

invoer = input('Geef een string van drie letters om deze om te keren: ')
reverse(invoer)
