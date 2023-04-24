import sys,time

print('''collatz sequence, or the 3n+1 Problem
 The collatz sequence is a sequence of numbers produced from starting number n, following three rules
 1) if n is even, the next number n is n/2.
 2) if n is odd, the next number n is n*3+1
 #) if n is 1, stop. Otherwise, repeat
 
 it is generally thought, but so far not mathematically proven that every starting number eventually terminates at 1.''')

print('Enter a staring number(greater than 0 or quit')
response=input('>?')
if not response.isdecimal() or response=='0':
    print('You must enter an integer greater than 0')
    sys.exit()
n=int(response)
print(n,end='', flush=True)
while n !=1:
    if n % 2 ==0: #if n is even..
        n=n//2
    else:
        n=3*n+1
    print(',  ' + str(n), end='',flush=True)
    time.sleep(0.1)
print()

