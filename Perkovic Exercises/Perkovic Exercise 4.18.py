s = '''It was the best of times, it was the worst of times; it was the age of wisdom, it was the age of foolishness; it was the epoch of belief, it was the epoch of incredulity; it was ...'''
newS = s.replace('.', ' ')
newS = newS.replace(',', ' ')
newS = newS.replace(';', ' ')
newS = newS.replace('\n', ' ')
newS = newS = newS.lower()

print(newS.count('it was'))
newS = newS.replace('was', 'is')
listS = newS.split()
print(listS)
print(newS)
