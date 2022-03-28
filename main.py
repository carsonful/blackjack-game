
# USES http://deckofcardsapi.com/?ref=devresourc.es'

# API FOUND ON https://www.devresourc.es/category/public-apis/games-and-comics
"""
IMPORTANT INFO FOR GAME / RULES OF BLACKJACK
To-Do:
- Set Jack,Aces,Kings and Queens to have Number Value
- Make One card hidden and allow users to hit or pass 
- Make a cash amount or beginning amount so the user can bet.
- Allow for users to users to keep track of there money and how much they can bet.
- Keep Console Clean
END, END GOALS -
- Sign in through website
- Save Data using DB
- Mobile friendly 
- Reward Users for coming back
"""
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
    return  msg + f', You now have ${money}.'





#def money(status):
    
# players.bet(status,bets)




print(play())

again = input('Would you like to play again? "Y" or "N": ')

while again != 'N':
    print(play())