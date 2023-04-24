l1=['eat','sleep','repeat']
b2='geeks'

obj1=enumerate(l1)
obj2=enumerate(b2)

print(list(obj1))
print(list(obj2))
for ele in enumerate(l1):
    print(ele)
for counter, ele in enumerate(l1,100):
    print(counter,ele)
import random
print(random.randint(1,2))

x='50'
txt=x.zfill(4)
print(txt)

colors=['black','red','white','blue']
fruits=['mango','apple','banana','grapes']
for i in colors:
    for l in fruits:
        print(i,l)
b=[]
for i in colors:
    b.append(i**2)
    print(b)