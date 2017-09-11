lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
middel = len(lst)/2
print(middel)


middel = int(middel)
print(lst[middel])

lst.reverse()
print(lst)

lst.remove(lst[0])
lst.append(14)
print (lst)
