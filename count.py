import collections

words = ['a', 'b', 'a', 'c', 'b', 'k']

c = collections.Counter(words)

print (c)

print (c.most_common(2))

print (c['i'])

def count_1 (a):
    a = collections.Counter(words).most_common(2)
    return (a)

print (count_1 (words))

##

d={}
for word in words:
    if word in ('a', 'b', 'h'):
        if word in d:
            d [word] += 1
        else:
            d[word] = 1

print(d)
