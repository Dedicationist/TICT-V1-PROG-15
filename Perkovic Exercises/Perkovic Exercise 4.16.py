invoer1 = input('Enter  first word: ')
invoer2 = input('Enter second word: ')
invoer3 = input('Enter second word: ')

lst = []
lst.append(invoer1)
lst.append(invoer2)
lst.append(invoer3)

lst2 = []
lst2.append(invoer1)
lst2.append(invoer2)
lst2.append(invoer3)

lst2.sort()

if lst == lst2:
    print('True')
