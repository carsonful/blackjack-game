
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






def play():

    x = players.dealer()
    bets = x[2]
    if x[0] > x[3]:
        status = 'LOSS'
        msg = f'Dealer Wins -${bets}'
    elif x[0] == x[3]:
        status = 'PUSH'
        msg = "It's a push keep your money!"
    elif x[0] < x[3]:
        status = 'WIN'
        msg = f'You win +${bets}'
    
    return players.bet(status,bets)







print(play())
