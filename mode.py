from collections import Counter

#also can import collections, but then also have to write collections.counter

a=[1,2,3,3,3,4,4,5,5,5,5,6,6,67,6,]

def mode_1(l):
    return Counter(l).most_common(2)[0]

print (mode_1(a))

# list, has specific commands append, extend, insert, more flexible

a=[1,2,3]

#tulip,

b=(1,2,3)

#accessing always []

print (a[2])
print (b[1])

