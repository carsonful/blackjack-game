
# USES http://deckofcardsapi.com/?ref=devresourc.es'

# API FOUND ON https://www.devresourc.es/category/public-apis/games-and-comics

import requests
from extensions import cards
from extensions import players


money = 500



def play():

    x = players.dealer()
    bets = x[2] # FOR BETS
    
    userspoints = x[3][0]
    dealerspoints = x[0]
    if userspoints > 21:
        status = 'LOSS'
        msg = f'Dealer Wins -${bets}'
    elif dealerspoints > 21:
        status = 'WIN'
        msg = f'You win +${bets}'
    elif dealerspoints > userspoints:
        status = 'LOSS'
        msg = f'Dealer Wins -${bets}'
    elif dealerspoints == userspoints:
        status = 'PUSH'
        msg = "It's a push keep your money!"
    elif dealerspoints < userspoints:
        status = 'WIN'
        msg = f'You win +${bets}'



    playersbet = players.bet(status, bets)
    money = playersbet[0]
    return  msg + f', You now have ${money}.', money





#def money(status):
    
# players.bet(status,bets)




x = play()

money = x[1]

print(x[0])



again = input('Would you like to play again? "Y" or "N": ')

while again != 'N':
    x = play()
    money = x[1]

    print(x[0])
