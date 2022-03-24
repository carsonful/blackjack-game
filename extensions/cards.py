import requests

URL = 'http://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'

r = requests.get(URL).json()


deckID = r['deck_id']



def draw_card():
    nonnumbers = {'KING', 'QUEEN', 'ACE', 'JACK'}
    URL =  f'http://deckofcardsapi.com/api/deck/{deckID}/draw/?count=1'
    card = requests.get(URL).json()
    card = card['cards']
    for info in card:
        suit = info['suit']
        if info['value'] in nonnumbers:
            value = 10
            if info['value'] == 'ACE':
                while True:
                    value = int(input('Would you like your ace to be 1 or 11: '))
                    if value == 11 or value == 1:
                        value = value
                        break
    return value, suit




def dealer():
    URL = f'http://deckofcardsapi.com/api/deck/{deckID}/draw/?count=1'
    card = requests.get(URL).json()
    card = card['cards']
    for info in card:
        secretcard = info['value'] + ' of ' + info['suit']
    
    card = requests.get(URL).json()
    card = card['cards']
    for info in card:
        upcard = info['value'] + ' of ' + info['suit']

    return upcard,secretcard

for i in range(52):
    print(draw_card())