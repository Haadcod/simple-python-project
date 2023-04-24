import random ,sys, time

#set up the constants:
WIDTH=70
PAUSE_AMOUNT=0.05
print('Deep cave')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth=20
gapWidth=10

while True :
    #displaythe tunnel segment
    rightWidth=WIDTH-gapWidth-leftWidth
    print(('#'*leftWidth)+('  '*gapWidth) + ('#' * rightWidth))
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    #Adjust the left side width
    diceRoll =random.randint(1,6)
    if diceRoll==1 and leftWidth > 1:
        leftWidth= leftWidth-1  #decrease theleftside width.
    elif diceRoll ==2 and leftWidth +gapWidth <WIDTH-1:
        leftWidth=leftWidth +1  #increase the leftside width
    else:
        pass  #Do nothing
