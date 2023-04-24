'''The caeser cipher is an incident encryption algorithm used by julius ceaser. It encrypts letters by shfting
them over by a certain number of places in the alphebet. we call the length of the shift the key. for example
,if the key is 3, then A becomes D, B becomes E, C becomes F and so on. To decrypt the message, you must shift
the encrypted letters in the oppsite direction. This program lets the user encrypt and decrypt messages
according to this algorithm.'''

"""like most cipher programs, the caesar cipher works by translating characters into numbers, performing 
some math operations on those numbers, and translating the numbers back into text characters. in the context 
of ciphers,we call these texts characters symbols. symbols can include letters, numeric digits and punctuations
amrks, each of which gets assigned a unique integer. In the case of the caeser cipher program, the symbols 
are all letters, and their integers are their position in the symbols string: 'ABCDEFGHIJKLMNOPRSTUVWXYZ"""
try:
    import pyperclip   #pyperclip copies text to the clipboard
except ImportError:
    pass  #if pyperclip is not installed, do nothing. Its no big deal.

#Every possible symbol that can be encryptred/decrypted:
# (!) you can add numbers and punctuation marks to encrypt those symbols as well.

SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The ceaser cipher encrypts letters by shifting them over by a')
print('key number. for example, a key of 2 means the letters A is ')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

#Let the user enter if they are encrypting or decrypting:
while True: #keep asking until the user enters e or d.
    print('Do you to (e)ncrypt or (d)ecrypt?')
    response =input('>').lower()
    if response.startswith(('e')):
        mode='encrypt'
        break
    elif response.startswith('d'):
        mode='decrypt'
        break
    print('please enter the the letter e or d.')

#let the user enter the key to use:
while True:  #keepasking until the user enters a valid key
    maxKey=len(SYMBOLS)-1
    print('please enter the key(0 t0 {}) to use'.format(maxKey))
    response=input('>').upper()
    if not response.isdecimal():
        continue
    if 0<=int(response)<len(SYMBOLS):
        key=int(response)
        break
#Let the user enter the message to encrypt
print('Enter the message to {}'.format(mode))
message=input('>?')
message=message.upper()
#stores the encrypted/decrypted form of the message:
translated=''

#Encrypt/decrypt each symbol in the message.
for symbol in message:
    if symbol in SYMBOLS:
        #Get the encrypted number or this symbol.
        num=SYMBOLS .find(symbol) #get the symbol
        if mode == 'encrypt':
            num=num + key
        elif mode=='decrypt':
            num=num-key
        #handle the wrap around if num larger than the length of symbols or less
        if num >=len(SYMBOLS):
            num=num -len(SYMBOLS)
        elif num < 0:
            num=num+len(SYMBOLS)
        #add encrypted/decrypted number's of symbol to translated:
        translated=translated + SYMBOLS[num]
    else:
        #just add the symbol without encrypting/decrytpting
        translated =translated + symbol
#Displaythe encrypted/decrytpted string to the screen:
print(translated)
try:
     pyperclip.copy(translated)
     print('Full {}edctext copied to clipboard.'.format(mode))
except:
     pass
