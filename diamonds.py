def main():
    print('Diamonds')

    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()
def displayOutlineDiamond(size):
    #Display the top half of the diamond.
    for i in range(size):
        print(' ' * (size - i - 1), end='')  #left side space.
        print('/', end='')  #left side of the diamond
        print('  ' * (i * 2), end='')  #interior of the diamond
        print('\\')  #right side of the diamond.
    #Display the bottom half of the diamond
    for i in range(size):
        print('  ' * i, end='')  #left side space.
        print('\\',end='')  #left side of the diamond
        print('  '*((size - i-1) *2),end='')  #interior of the diamond
        print('/')  #right side of the diamond

def displayFilledDiamond(size):
    #Display the top half of the diamond:
    for i in range(size):
        print(' ' *(size -i -1),end='')  #left side space.
        print('/' * (i + 1),end='')  #left half of diamond
        print('\\' * (i+1))  #right half of the diamond
    #display thebottom half of the diamond
    for i in range(size):
        print('  ' *i, end='')  #left side space
        print('\\' * (size-i), end='')  #left side of diamond.
        print('/' *  (size-i))  #right side of the diamond.
if __name__=='__main__':
    main()
