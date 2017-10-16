mult3 = set()
mult5 = set()
mult7 = set()
som3 = 0
som5 = 0
som7 = 0

for i in range(100):
    som3 += 3
    mult3.add(som3)
    som3 += 5
    mult3.add(som5)
    som3 += 7
    mult3.add(som7)

print(mult3)
