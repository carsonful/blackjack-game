from extensions import cards
import time

money = 500

def user():
    
    
    named_cards = {'K', 'Q', 'J'}


    card1 = cards.define_card()
    card2 = cards.define_card()

    hand = [card1, card2]

    total = 0
    while total <= 21:
        total = 0

        for i in range(len(hand)):
            card = hand[i] 
            value = card[0]
            suit = card[1]
            if value in named_cards:
                total = total + 10
                cards.show(value,suit)
            elif value == 'A':
                cards.show(value,suit)
                ace = 0
                while ace != 11 and ace != 1:
                    ace = int(input('Would you like the Ace to be a 1 or 11: '))
                
                total += ace
            else:
                total += int(value)
                cards.show(value,suit)


        if total > 21:
            print(f'{total}, You Busted!')
            break
        print(total)


        move = input('Put "H" for hit or "S" for stand. :').upper()
        if move == 'H':
            print('You have chosen to Hit!')
            hand.append(cards.define_card())
        elif move == 'S':
            print('You have chosen to Stand!')
            break
            
    
    return total, hand








def bet(status, bet_amount):
    bets = bet_amount
    message = status
    if status == 'WIN':
        bets = bets + money
        message =  f'Congrats you now have ${bets}'
    elif status == 'LOSS':
        bets = money - bets
        message =  f'Good try you now have ${bets}'
    elif status == 'PUSH':
        message =  f'Good Try you have ${bets}'
        bets = money
        pass
    return bets, message
    

def dealer():

    
    
    bets = int(input(f'How much would you like to bet? (Money: ${money}):'))


    card1 = cards.define_card()
    card2 = cards.define_card()

    named_cards = {'K', 'Q', 'J'}
    
    hand = [card1, card2]
    count = 0
    total = 0
    while total <= 21:
        total = 0

        for i in range(len(hand)):
            card = hand[i]
            value = card[0]
            suit = card[1]
            if count == 1:
                if i == 1:
                    cards.show('X','X')
                    print('^^^^^^DEALERS HAND^^^^^^')

            elif value in named_cards:
                total += 10
                cards.show(value, suit)
            elif value == 'A':
                cards.show(value, suit)
                if total < 16:
                    ace = 10
                elif total >= 16:
                    ace = 1
                total += ace
            else:
                total += int(value)
                cards.show(value, suit)
        
            
            if count == 1:
                compare = user()
                print('^^^^^YOUR HAND^^^^^')
                count = count + 1
                pass
            count = count + 1

        print(total)    

        if total < 16:
            print('The Dealer Hits!')
            hand.append(cards.define_card())
        elif total > 21:
            print('The dealer has busted!')
            break
        else:
            print('The dealer stands!')
            break
        


    return total, hand, bets, compare


