
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
- Mobile friendly (possibly lol)
- Reward Users for coming back


"""
import requests

URL = 'http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'

r = requests.get(URL).json()


DECKID = r['deck_id']

card_count = r['remaining']

for i in range(card_count):
    URL = f'http://deckofcardsapi.com/api/deck/{DECKID}/draw/?count=1'

    card = requests.get(URL).json()
    card = card['cards']
    for info in card:
        print(info['value'] + ' of ' + info['suit'])





