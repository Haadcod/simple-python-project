import copy, random,sys,time

#setup constants
WIDTH=79   #Width of the cell grid
HEIGHT=20 #The hiegth of the cell grid

ALIVE='O' #The character representing the living cell
DEAD=''

#The cells and next cells are dictionaries for the state of the game
#Tehir keys are x,y tuples and their values are one of the alive or dead values

nextcells={}
#Put random alive and dead cells into nextcells:
for x in range(WIDTH):  #Loop over every possible column.
    for y in range(HEIGHT): #Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead
        if random.randint(0,1)==0:
            nextcells[(x,y)]=ALIVE #Add a living cell.
        else:
            nextcells[(x,y)]=DEAD #Add a dead cell.
while True: #mainloop.
    #Each iteration of this loop is a step of the simulation.
    print('\n'*50)  #sepearate each step with newlines.
    cells=copy.deepcopy(nextcells)

    #print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end='')  #print the # or space.
        print()  #print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    #calculate the next step' cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get the neighbouring coordinates of (x,y), even if they wrap around the edge:
            left=(x-1) % WIDTH
            right=(x+1) %WIDTH
            above=(y-1) %HEIGHT
            below=(y+1) %HEIGHT
            #count the number of living neighbours

            numNeighbours=0
            if cells[(left,above)]==ALIVE:
                numNeighbours +=1  #Top-left neighbour is alive.
            if cells[(x,above)]==ALIVE:
                numNeighbours+=1  #Top neighbour is alive.
            if cells[(right,above)]==ALIVE:
                numNeighbours+=1   #Top_right neighbour is alive
            if cells[(left,y)]==ALIVE:
                numNeighbours+=1   #Left neighbour is alive
            if cells[(right,y)]==ALIVE:
                numNeighbours+=1   #Right neighbour is alive
            if cells[(leeft)]

