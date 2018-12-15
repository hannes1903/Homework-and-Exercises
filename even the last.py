import math
import statistics

b = [1,2,4,5,6,7,8,9,6,6,4,5,]

print(len(b))

list2=b[0::2]

print (list2)

list3=sum(list2)*b[-1]

print (list3)

def checkio(V):
    a=len(V)
    if a==0:
        return (0)
    else:
        list2=V[0::2]
        list3=sum(list2)*V[-1]
    return (list3)

print (checkio(b))