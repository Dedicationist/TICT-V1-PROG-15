def vowels(string):
    for i in range(0, len(string)):
        if string[i] in 'aeiouAEIOU':
            print(i)

invoer = input('Geef een willekeurige string: ')
vowels(invoer)
