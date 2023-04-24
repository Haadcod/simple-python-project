import random

num_digit=3
max_number=10

def main():
    print('I am thinking of a {}-digit with no repeated values.'.format(num_digit))
    print(getSecreteNum())
if __name__=='__main__':
    main()
def getSecreteNum():
    numbers=list('0123456789')
    random.shuffle(numbers)
    secretNum=''
    for i in range(num_digit):
        secretNum+=str(numbers)

