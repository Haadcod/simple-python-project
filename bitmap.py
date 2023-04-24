'''This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel,to determine
how it should display a message from the user. in this bitmap,space characters represent an empty space and all
other characters a replaced by characters in users message. The provided bitmap represents a world map, buh you can change this
to any kind of image you wud like. The binary simplicity of the space or message characters systems makes it good for
biginners. try experimenting with different messages to see the result'''

'''instead of typing each character of the world map pattern, you can copy and paste the whole thing . A line of 68 periods 
at the top and bottom of the pattern acs as a ruler to help you align it correctly.However the program will still work
if you make typos in the pattern.
The bitmap.splitlines() method call returns a list of strings, each of which is a line in the multiline bitmapstring. using 
a multiline string makes the bitmap easir to edit into whatever pattern you like. The program fills in the space 
character in the pattern which is why the sterik, periods or any other character do the same thing.
the bitmap message[i %len(message)] causes repetition of the text in message. As i increases from 0 to a number 
larger than len(message), the expression i %len(message) evaluates to 0 again. This causes messaage[i % len(message)],
to repeat the characters in message as i increases.'''

import sys

bitmap='''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''
print('Bitmap message.')
print('Enter the message to display the bitmap.')

message=input('>')
if message =='':
    sys.exit()
#loop for every each line in a bitmap
for line in bitmap.splitlines():
    #loop over each character in the line
    for i,bit in enumerate(line):
        if bit==' ':
            #print an empty space since therez a space in the bitmap
            print(' ',end='')
        else:
            print(message[i % len(message)],end='')
    print()
