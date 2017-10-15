def case(string):
    if string[0] == string.capitalize()[0]:
        return 'capitalized'
    elif string[0] == string.lower()[0]:
        return 'not capitalized'
    else:
        return 'unknown'

#print(case('Enno'))
#print(case('enno'))
#print(case('3nno'))
