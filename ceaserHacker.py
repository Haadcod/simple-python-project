"""This program can hack messages encrypted with ceaser cipher wothout you even knowing the code
There are only 26 possible keys for a ceaser cipher so the computer can easily try all possible
decryptions and display the results to the user. This is called brute_force attack."""

print('Ceaser cipher hacker')
#Let the user specify the message to hack
print('Enter the ceaser cipher message to hack')
message=input('>?')

#Every possible symbol that can be encrypted/decrypted. This must match the symbols used in ceaser cipher

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated=''

    #Decrypt each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            num=SYMBOLS.find(symbol) #get the number of symbol
            num=num-key  #Decrypt the number

            #handle the wrap-around if num is less than zero
            if num<0:
                num=num+len(SYMBOLS)
            #Add the decrypted number's symbol to translated
            translated=translated+SYMBOLS[num]
        else:
            #just add the symbol without decrypting
            translated=translated+symbol
    #display the key being,being tested, along with its decrypted text
    print('Key #{},{}'.format(key,translated))
