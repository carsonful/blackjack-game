from unicodedata import digit
import requests

URL = 'http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=3'

r = requests.get(URL).json()


deckID = r['deck_id']


def define_card():

    URL = f'http://deckofcardsapi.com/api/deck/{deckID}/draw/?count=1'
    card = requests.get(URL).json()
    card = card['cards']

    for info in card:
        value = info['value']
        suit = info['suit'] 

        if suit == 'SPADES':
            suit = '♠'
        elif suit == 'HEARTS':
            suit = '♥'
        elif suit == 'CLUBS':
            suit = '♣'
        elif suit == 'DIAMONDS':
            suit = '♦'

        if value is not digit:
            value = value[0]
            



    return value, suit


def show(value, suit):
    print('┌───────┐')
    print(f'| {value:<2}    |')
    print('|       |')
    print(f'|   {suit}   |')
    print('|       |')
    print(f'|    {value:>2} |')
    print('└───────┘') 



def hit():
    define_card()





def shuffle_deck():
    URL = f'http://deckofcardsapi.com/api/deck/{deckID}/shuffle/'
    print(URL)
    shuffledeck = requests.get(URL).json()