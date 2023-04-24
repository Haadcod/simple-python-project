"""bagels, sa deductive logic game. you must guess a three secrete digit number based on clues.
The game offers one of the following hints in response to your guess: "Pico when your guess has
a correct digit in the wrong place "Fermi when your guess has a correct digit in the correct place
,"Bagels" if your guess has no correct digits. you have 10 tries to guess the number.
"""
import random

NUM_DIGITS=3
MAX_DIGITS=10

def main():
    print('''bagles, deductive logic game I am looking for 3 digit number. Try to guess what it is. Here are some clues.
          when i say:      That means:

          Pico             one digit is correct but in the wrong place
          fermi            one digit is correct but in the right position
          bagle            no digit is correct''')

          while True:  #main game loop.
            #this stores the secrete number the player needs to guess
            print('i have thought of a number.')
def getScreteNumber():
    """returns string made up of NUM_DIGITS unique random numbers"""
    numbers=list('0123456789')  #create list of digits 0 to 9
    random.shuffle(numbers)  #shufflr them into random order
    #Get the fir first num_digits in the list for the secrete number.
    secretNum=''
    for in range(NUM_DIGITS):
      
        

