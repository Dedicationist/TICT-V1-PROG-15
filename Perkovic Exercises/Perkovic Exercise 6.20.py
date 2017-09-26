def reverse(book):
    reversebook = {}
    for woorden in book:
        reversebook[book[woorden]] = woorden
    return reversebook



print(reverse({'Smith, Jane': '123-45-67','Doe, John':'987-65-43','Baker, David':'567-89-01'}))
