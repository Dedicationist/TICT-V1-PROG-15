answers = ['Y','N','N','Y','N','Y','Y','Y','N','N','N']
numYes = answers.count ('Y')
print (numYes)
numNo = answers.count ('N')
percentYes = (numYes / 11) * 100
print (percentYes)
answers.sort
f = answers.index ('Y')
print (f)

