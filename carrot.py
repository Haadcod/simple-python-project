import random
print('''carrot in the box
This is a buffuling game for two human players. Each player has a box. One box has a carrot in it.
You must have the box with the carrot in it.
This is a stupid and silly game

the first player looks into the box(The second player must close their eyesduring this time).The first player then says there 
is a carrot in the box he picked or there is not a crrot in my box. the second player gets to decide 
if they want to swap boxes or not........''')
input('Please press enter to beging.....')

p1Name=input('Human player1, enter your name:')
p2Name=input('Human player2, enter your name:')
playerNames=p1Name[:11].center(11) + '    ' + p2Name[:11].center(11)

print('''HERE ARE THE TWO BOXES:
   __________     __________
   /         /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ',you have a red box infront of you.')
print(p2Name + ',you have a gold box infront of you.')
print()
print(p1Name + ', you will get to look into the box.')
print(p2Name.upper() + ',close your eyes and dont look!!!')
input('When ' + p2Name.upper() + ' has closed their eyes, press Enter........')
print()

print(p1Name + ' here is the inside of your box:')

if random.randint(1,2)==1:
    carrotInFirstBox=True
else:
    carrotInFirstBox=False
if carrotInFirstBox:
    print('''
    ___VV____
    |   VV    |
    |   VV    |
    |___||____|    __________
   /    ||   /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/
  (carrot!)''')
    print(playerNames)
else:
    print('''
    |         |
    |         |
    |_________|    __________
   /         /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/
  ( no carrot!)''')
    print(playerNames)
input('Press enter to continue...')

print('\n'*100) #clear the screen by printing several lines.
print(p1Name + ' ,say one of the following sentences to ' + p2Name + '.')
print('  1) There is a carrot in my box.')
print('  2) There is no carrot in my box')
print()
input('Press enter to continue....')

print()
print(p2Name.upper() + ', Do you want to swap boxes with ' + p1Name.upper() + '? YES/NO .')
while True:
    response=input('>?').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', Please enter "YES or NO".')
    else:
        break
firstBox= 'RED'  #Note the space after the 'D'
secondBox= 'GOLD'

if response.startswith('Y'):
    carrotInFirstBox= not carrotInFirstBox
    firstBox,secondBox=secondBox,firstBox

print('''HERE ARE THE TWO BOXES:
  __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox,secondBox))
print(playerNames)

input('Press enter to continue...')
print()
if carrotInFirstBox:
    print('''
    ___VV____      _________
   |   VV    |    |         |
   |   VV    |    |         |
   |___||____|    |_________|
  /    ||   /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox,secondBox))
else:
    print('''
    _________      ___VV____
   |         |    |   VV    |
   |         |    |   VV    |
   |_________|    |___||____|
  /         /|   /    ||   /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(firstBox,secondBox))
print(playerNames)
#This modification made possible through the 'carrotinFirstBox variable'
if carrotInFirstBox:
    print(p1Name.upper() + ',is the winner!')
else:
    print(p2Name.upper() + ', is the winner!')
print('Thanks for playing!')
