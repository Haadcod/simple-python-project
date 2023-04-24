import random, sys

QUESTIONS=[
    {'question':'How many times can you take 2 apples from a pile of 10 apples?',
     'answer':'once. Then you have a pile of 8 apples',
     'accept':['once','one','1']},
    {'question':'what begins with "e" and ends with "e" but only has one letter in it?',
     'answer':'An envelope.',
     'accept':['envelope']},
    {'question':'is it possible to draw a square with three sides?',
     'answer':'yes. all squares have three sides. They also have a fourth side.',
     'accept':['yes']},
    {'question':'How many timescan a piece of paper be folded in half by hand without unfolding?',
     'answer':"once. Then you are folding it in quarters.",
     'accept':['one','1','once']},
    {'question':'what does a towel get as it dries?',
     'answer':"Drier.",
     'accept':['drier','dry']},
    {'question':'Imagine you are in a haunted house full of evil ghosts. What do you have to do to stay safe?',
     'answer':'She was walking.',
     'accept':['Wet']},
    {'question':"The clerk at the butcher shop is exactly 177 centiment",
     'answer':'The clerk weighs meat',
     'accept':['meat']}
]

CORRECT_TEXT=['Correct!','That is right.',"you're right.",'you got it.','Righto!']
INCORRECT_TEXT=['incorrect!','Nope, that isnt it.','Nope.','Not quite.','You missed it.']

print('''Trick questions,
Can you igure out the answers to these trick questions?
(Enter QUIT to quit at any time.)''')

input('Press Enter to begin...')
random.shuffle(QUESTIONS)
score=0

for questionNumber,qa in enumerate(QUESTIONS):
    print('\n'*40)  #"Clear" the screen.
    print('Question:',questionNumber+1)
    print('Score:', score, '/', len(QUESTIONS))
    print('QUESTION:',qa['question'])
    response=input('   ANSWER:  ').lower()

    if response =='quit':
        print('Thanks for playing!')
        sys.exit()

    correct=False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct=True
    if correct:
        text=random.choice(CORRECT_TEXT)
        print(text,qa['answer'])
        score +=1
    else:
        text=random.choice(INCORRECT_TEXT)
        print(text,'The answer is:',qa['answer'])
    response=input('Press Enter for the next question...').lower()
    if response =='quit':
        print('Thanks for playing!')
        sys.exit()
print("That's all the questions. Thanks for playing!")
