lst = eval(input('Put in a list of student names: '))
for names in lst:
    if names[0] in 'abcdefghijklm' or names[0] in 'ABCDEFGHIJLM':
        print(names)


#['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
