
a = 'prom'
b = 'prom'

c=a.lower()
d=b.lower()

def sortieren(c, d):
    if sorted(c)==sorted(d):
       return 'true'
    else:
       return 'false'

print (sortieren(c, d))

print (sorted(c)==sorted(d))

###


def compare(a, b):
    if len(a)!= len (b):
        return False

    abc = [0] * 256
    for c in a:
        abc[ord(c)] += 1

    for c in b:
        abc[ord(c)] -= 1
        if abc[ord(c)] < 0:
            return False

    return True

print(compare(a, b))

####

def compare1(a, b):

    abc = [0] * 256
    for c in a:
        abc[ord(c)] += 1

    for c in b:
        abc[ord(c)] -= 1
        if abc[ord(c)] < 0:
            return False

    for letter in abc:
        if letter != 0:
            return False

    return True

print(compare1(a, b))

