'''The card suit symbols dont exist on your keyboard, hich is hy we call the chr() function
to create them. The integer passed to the char() function is called uniccode code point a
unique number that identifies a character according to the unicode standard. unicode is often misunderstood. However Batchelder's gave a code introduction to uncode'''
'''The classic game is also known as 21'''

import random, sys

#set up constants
HEARTS=chr(9829)
DIAMONDS=chr(9830)
SPADES=chr(9824)
CLUBS=chr(9827)
BACKSIDE='backside'

def main():
    print('''blackjerk rules:
    Try to get as close to 21 without going over.
    kings, queens, and jacks are worth 10 points. 
    Aces are worth 1 or 11 points.
    cards 2 through 10 are worth their face values.
    (H)it to take another card.
    (S)tand to stop taking cards.
    on your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
    incase of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')
    money=5000
    while True:
        #Check if player has run out of money
        if money <=0:
            print('You are broke!')
            print('Good thing you were not playing with your money.')
            print('Thanks for playing!')
            sys.exit()
        #let theplayer enter their bet for this round
        print('money',money)
        bet=getBet(money)

        #Give the dealer and player 2 cards from the deck each:
        deck=getDeck()
        dealerHand=[deck.pop(),deck.pop()]
        playerHand=[deck.pop(),deck.pop()]

        #handle player actions
        print('Bet',bet)

        while True: #keep looping untill player stands or busts.
            displayHands(playerHand,dealerHand,False)
            print()

            #Check if player has bust:
            if getHandValue(playerHand) >21:
                break
            #get the players move, either H,S,or D;
            move =getMove(playerHand,money-bet)

            #handle players action:
            if move=='D':
                #player is doubling down, they can increase their bet:
                additionalBet= getBet(min(bet,(money-bet)))
                bet +=additionalBet
                print('Bet increased to {}.'.format(bet))
                print('bet:',bet)
            if move in ('H','D'):
                #Hit/doubling down they can increase their bet:
                newCard =deck.pop()
                rank,suit=newCard
                print('you drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) >21:
                    #The player has busted :
                    continue
                if move in ('S','D'):
                    #Stand/doubling down stops the player's turn.
                    break
            #handle the dealer's actions:
            if getHandValue(playerHand) <=21:
                while getHandValue(dealerHand) <17:
                    #The dealer hits:
                    print('Dealer hits...')
                    dealerHand.append(deck.pop())
                    displayHands(dealerHand,playerHand,False)

                    if getHandValue(dealerHand) >21:
                        break #The dealer has busted.
                    input('Press Enter to continue...')
                    print('\n\n')
            #show  the final hands:
            displayHands(playerHand,dealerHand,True)
            playerValue=getHandValue(playerHand)
            dealerValue=getHandValue(dealerHand)

            #handle whether the player won,lost,or tied
            if dealerValue>21:
                print('Dealer busts! You win ${}!'.format(bet))
                money +=bet
            elif(playerValue>21) or (playerValue<dealerValue):
                print('you lost!')
                money-=bet
            elif playerValue > dealerValue:
                print('you won ${}!'.format(bet))
                money +=bet
            elif playerValue==dealerValue:
                print('it\s a tie, the bet is returned to you.')
            input('press Enter to continue...')
            print('\n\n')



def getBet(maxBet):
    '''Ask the player how much they want to bet for this round.'''
    while True:  #keep asking untill they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT'.format(maxBet))
        bet=input('>').upper().strip()
        if bet=='QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue #if player didnot enter a number, ask again.
        bet=int(bet)
        if 1<=bet<=maxBet:
            return bet #player entered a valid bet
def getDeck():
    '''Return a list of (rank,suit) tuples for all 52 cards.'''
    deck=[]
    for suit in (HEARTS,DIAMONDS,SPADES,CLUBS):
        for rank in range(2,11):
            deck.append(str(rank),suit)  #Add the numbered cards.
        for rank in ('J','Q','K','A'):
            deck.append(rank,suit)   #Add the face and ace cards.
    random.shuffle(deck)
    return deck
def displayHands(playerHand,dealerHand,showDealerHand):
    '''Show the player and dealers cards. Hide the dealers first card if showDealer is False.'''
    print()
def getHandValue(cards):
    '''Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1(function picks most suitable value)'''
    value=0
    numberOfAces=0

    #Add value for non ace cards
    for card in cards:
        rank=card[0]  #card is a tuple like(rank,suit)
        if rank=='A':
            numberOfAces+=1
        elif rank in ('K','Q','J'):  #face cards are worth 10 points.
            value+=10
        else:
            value+=int(rank) #Numbered cards are worth their number.
    #add value for aces:
    value+=numberOfAces #Add 1 per ace.
    for i in range(numberOfAces):
        #if another 10 can be added without busting then do so.
        if value + 10<=21:
            value +=10
    return value


def displayCards(cards):
    '''Display all cards in the list.'''
    rows=['','','','','']  #The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] +='__ ' #print the top line of the card
        if card==BACKSIDE:
            #print cards backside
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            #print the cards front:
            rank,suit=card #This card is a tuple data structure.
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(rank.suit)
            rows[3] += '|_{}|'.format(rank.rjust(2,'_'))
    #print each row on the screen
    for row in rows:
        print(row)
def getMove(playerHand,money):
    '''Asks th player for their move and returns 'H' for hit,'S' for stand and 'D' for double down'''
    while True: #keep looping until player enters a correct move.
        #determine what moves the player can make.
        moves=['(H)it','(S)tand']

        #The player can double down their first move, which we can tell because they'll have exactly two cards
        if len(playerHand)==2 and money>0:
            moves.append('(D)ouble down')
        #get players move:
        movePrompt=' '.join(moves) +'>'
        move=input(movePrompt).upper()
        if move in ('H','s'):
            return move  #player entered a valid move
        if move=='D' and '(D)ouble down ' in moves:
            return move #player has entered a valid move
if __name__=='__main__':
    main()