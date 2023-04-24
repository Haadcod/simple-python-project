'''seven segment number display module countdown and digital clock prgrams.'''

def getSevSegStr(number,minWidth=0):
    '''Return a seven-segment display string of number. The returned string will be padded with zeros if it is smaller than minWidth. '''
    #convert number to string incase its an int or float:

    number=str(number).zfill(minWidth)
    rows=['','','']
    for i,numeral in enumerate(number):
        if numeral=='.':  #Render the decimal point.
            rows[0]+='  '
            rows[1]+='  '
            rows[2]+='  '
            continue  #skip the space between the digtis
        elif numeral=='_': #render the negative sign:
            rows[0]+='   '
            rows[1]+='   '
            rows[2]+=' __'
        elif numeral=='0': #render the 0:
            rows[0]+=' __ '
            rows[1]+='|  |'
            rows[2]+='|__|'
        elif numeral=='1': #render the 1:
            rows[0]+='    '
            rows[1]+='   |'
            rows[2]+='   |'
        elif numeral=='2': #render the 2:
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+='|__ '
        elif numeral=='3': #render the 3:
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+=' __|'
        elif numeral=='4': #render the 4:
            rows[0]+='    '
            rows[1]+='|__|'
            rows[2]+='   |'
        elif numeral=='5': #render the 5:
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+=' __|'
        elif numeral=='6': #render the 6:
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+='|__|'
        elif numeral=='7': #render the 7:
            rows[0]+=' __ '
            rows[1]+='   |'
            rows[2]+='   |'
        elif numeral=='8': #render the 8:
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+='|__|'
        elif numeral=='_': #render the negative sign:
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+=' __|'

        #Add a space(for the space in between numerals ) if this isnt the last numeral and the decimal point isnt next:
        if 1 != len(number) -1 and number[i+1] != '.':
            rows[0] +=' '
            rows[1] +=' '
            rows[2] +=' '
    return '\n'.join(rows)

#if this program isnt imported display the numbers 00 to 99.
if __name__=='__main__':
    print('This module is meant to be imported rather than run.')
    print('For example this code.')
    print('import sevseg')
    print('myNumber=sevseg.getSevSegStr(42,3')
    print('print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print('                   ')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
