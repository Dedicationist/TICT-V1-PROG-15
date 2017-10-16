import random
def coin():
    HeadsOrTails = random.randrange(0, 2)
    if HeadsOrTails == 1:
        return 'Heads'
    else:
        return 'Tails'

print(coin())


