import sys
try:
     import pyttsx3
except ImportError:
     print('The pyttsx3 module needs to be installed to run this .')
     print('program. On linux, open a command prompt and run:')
     print('Pip3 install pyttsx3')
     sys.exit()
tts=pyttsx3.init()   #Initialise the TTS engine.

print('Text To Speech Talker.')
print('Text_to_speech using the pytts3 module, which turn uses')
print('the NSSpeechSynthesizer (on macOS)SAPI5(on windows),or')
print('eSpeak (on linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text=input('>?')
    if text.upper()=='QUIT':
        print('Thanks for playing!')
        sys.exit()
    tts.say(text)
    tts.runAndWait()
