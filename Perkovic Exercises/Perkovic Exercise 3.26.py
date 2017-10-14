lst = eval(input('Please give an input (list): '))
if lst == None:
    print('That\'s an empty list... How do you suppose I can give you the first and last element of nothing?')
else:
    print('The first list element is {}'.format(lst[0]))
    print('The last list element is {}'.format(lst[len(lst) - 1]))

#[3, 5, 7, 9]
