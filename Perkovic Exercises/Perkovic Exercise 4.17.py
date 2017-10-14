message = 'The secret of this message is that it is secret'
length = len(message)
count = message.count('secret')
censored = message.replace('secret', 'xxxxxx')

print(message)
print(length)
print(count)
print(censored)
