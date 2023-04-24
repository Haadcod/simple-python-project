import random,sys

JAPANESE_NUMBERS ={1:'ICH',2:'NI',3:'SAN',4:'SHI',5:'GO',6:'ROKU'}

print('''CHOHAN
In this traditional japanese dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor.
The player must guess if the dice total to an even (cho) or odd (han) number.''')
purse=5000
while True:
    #place your bet
    print('You have', purse, 'mon.How much do you bet? (or QUIT)')
    while True:
        pot=input('>')
        if pot.upper()=='QUIT':
            print('Thanks for playing')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number!')
        elif int(pot)>purse:
            print('You dont have enough to make that bet')
        else:
            #This is a valid bet
            pot=int(pot)
            break
    #Roll the dice
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the dice and asks for your bet.')
    print()
    print('   CHO (even) or HAN(odd)?')

    #let the player bet han or cho
    while True:
        bet=input('>').upper()
        if bet != 'CHO' and bet !='HAN':
            print('please enter either "CHO" or "HAN".')
            continue
        else:
            break
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '_', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '_', dice2)

    #determine if the player won:
    rollsEven = (dice1 + dice2) % 2==0
    if rollsEven:
        correctBet='CHO'
    else:
        correctBet='HAN'
    playerWon=bet==correctBet

    #display the results
    if playerWon:
        print('you won! You take',pot,'mon')
        purse=purse+pot
        print('The house collects a ', pot // 10, 'mon fee.')
        purse=purse-(pot//10) #The house fee is 10%
    else:
        purse=purse=pot
        print('You lost')
    #check if player has run out of money
    if purse==0:
        print('you have run out money!')
        print('Thanks for playing!')
        sys.exit()

