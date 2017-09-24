def rps(player1, player2):
    if player1 == player2:
        return 0
    elif player1 == 'R' and player2 == 'S':
        return -1
    elif player1 == 'R' and player2 == 'P':
        return 1
    elif player1 == 'S' and player2 == 'R':
        return 1
    elif player1 == 'S' and player2 == 'P':
        return -1
    elif player1 == 'P' and player2 == 'S':
        return 1
    elif player1 == 'P' and player2 == 'R':
        return -1

player1 = input('R, P or S?')
player2 = input('R, P or S?')
print(rps(player1, player2))

