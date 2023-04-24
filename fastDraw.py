import sys,random,time

print('Fast Draw')
print()
print('Time to test your relexes and see if you are the fastest')
print('Draw in the west')
print('When you see, you have 0.3 seconds to press enter')
print('but you loose if you press enter "DRAW" appears.')
print()
input('Press enter to begin...')

while True:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20,50)/10.0)
    print('DRAW!')
    drawTime=time.time()
    input()  #This function call doesnt return untill Enter is pressed
    timeElapsed=time.time()-drawTime

    if timeElapsed < 0.01:
        #if the player pressed Enter before DRAW! appeared the input call returns almost instantly.
        print('You drew before "DRAW" appeared! You lose.')
    elif timeElapsed >0.3:
        timeElapsed=round(timeElapsed,4)
        print('You took',timeElapsed,'seconds to draw. Too slow')
    else:
        timeElapsed=round(timeElapsed,4)
        print('You took',timeElapsed,'seconds to draw.')
        print('You are the fasted draw in the west!,You win!')
    print('Enter QUIT to stop or press Enter to play again')
    response=input('>').upper()
    if response=='QUIT':
        print('Thanks for playing!')
        sys.exit()