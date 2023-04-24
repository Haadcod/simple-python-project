'''This program has several functions for generating different kinds of clickbait headlines'''

import random

#set up constants

OBJECT_PRONOUNS=['Her','Him','Them']
POSSESIVE_PRONOUNS=['Her','His','Their']
PERSONAL_PRONOUNS=['She','He','They']
STATES=['Calfonia','Texas','Florida','New york','Pennsylaviana','Illinios','Ohio','Geogiana','North calorina',
        'Michigan']
NOUNS=['Athlete','Clown','Shovel','Paleo Diet','Doctor','Parent','Cat','Dog','Chicken','Robot','Video Game','Avocado',
       'Plastic Straw','Serial killer','Telehone psychic']
PLACES=['House','Attic','Bank Deposit Box','School','Basement','workplace','Donout shop','Apocalypse Bunker']
WHEN=['soon','This year','Later Today','Right Now','Next week']

def main():
    print('clickBait headline generator.')
    print()
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter a number of clickbait headlines to generate:')
        response=input('>?')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadline=int(response)
            break
    for i in range(numberOfHeadline):
        clickBaitType=random.randint(1,8)
        if clickBaitType==1:
            headline=generateMillenialSkillHeadline()
        elif clickBaitType==2:
            headline=generateWhatYouDontKnowHeadline()
        elif clickBaitType==3:
            headline=generateBigCompaniesHateHeadline()
        elif clickBaitType==4:
            headline=generateYouWontBelieveHeadline()
        elif clickBaitType==5:
            headline=generateWhatYouDontKnowHeadline()
        elif clickBaitType==6:
            headline=generateGiftHeadline()
        elif clickBaitType==7:
            headline=generateReasonsWhyHealdine()
        elif clickBaitType==8:
            headline=generateJobAutomateHeadline()
        print(headline)
    print()
    website=random.choice(['Website','blag','FaceBook','Googles','facebuuk','Tweedie','pastgram'])
    when=random.choice(WHEN).lower()
    print('Post these to our ',website, when, 'or you\'re fired!')

#Each of these functions returns a different type is headline
def generateMillenialSkillHeadline():
    noun=random.choice(NOUNS)
    return 'Are millinials killing the {} industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun=random.choice(NOUNS)
    pluralNoun=random.choice(NOUNS) + 's'
    when=random.choice(WHEN)
    return 'Without This {} ,{} could kill you {}'.format(noun,pluralNoun,when)
def generateBigCompaniesHateHeadline():
    pronoun=random.choice(OBJECT_PRONOUNS)
    state=random.choice(STATES)
    noun1=random.choice(NOUNS)
    noun2=random.choice(NOUNS)
    return 'Big companies hate {} ! see How This {} {} invented a chapter {}'.format(pronoun,state,noun1,noun2)
def generateYouWontBelieveHeadline():
    pluralNoun1=random.choice(NOUNS) + 's'
    pluralNoun2=random.choice(NOUNS) + 's'
    return 'What {} Don\t want you to know about {}'.format(pluralNoun1,pluralNoun2)
def generateGiftHeadline():
    number=random.randint(7,15)
    pluralNoun=random.choice(NOUNS)
    state=random.choice(NOUNS)
    state=random.choice(STATES)
    return '{} gift ideas to Give your {} From {}'.format(number,pluralNoun,state)
def generateReasonsWhyHealdine():
    number1=random.randint(3,19)
    pluralNoun=random.choice(NOUNS) + 's'
    #number2 should be nolonger than number1
    number2=random.randint(1,number1)
    return '{} Reasons Why {} Are more interesting than yiu think (Number {} will suprise you!)'.format(number1,pluralNoun,number2)
def generateJobAutomateHeadline():
    state=random.choice(STATES)
    noun=random.choice(NOUNS)

    i=random.randint(0,2)
    pronoun1=POSSESIVE_PRONOUNS[i]
    pronoun2=PERSONAL_PRONOUNS[i]
    if pronoun1=='Their':
        return 'This {} {} Didn\'t Think Robots would take {} Job. {} were wrong.'.format(state,noun,pronoun1,pronoun2)
    else:
        return 'This {} {} Din\'t Think Robots would take {} job. {} was wrong'.format(state,noun,pronoun1,pronoun2)

    #if the progrma is run instead of imported),run the game:
if __name__=='__main__':
    main()
