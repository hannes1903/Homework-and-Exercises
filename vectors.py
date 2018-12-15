a=[3, 5, 1]
b=[6, 1, 8]

def vector_add(v1):
    r=[]
    for i in range(len(v1)):
        r.append(v1[i])
    return r

print (vector_add(a))


def vector_add(v1, v2):
    r=[]
    for i in range(len(v1)):
        r.append(v1[i] + v2[i])
    return r

print (vector_add(a, b))



def vector_add(v1, v2):
        r = []
        for i, el in enumerate (v1):
            r.append(el + v2[i])
        return r

print (vector_add(a, b))


def vector_add(v1, v2):
    r = []
    for e1, e2 in zip(v1, v2):
        r.append (e1 + e2)
    return r

print(vector_add(a, b))

# before intended block always :


def vector_add(v1, v2):
    return [e1 + e2 for e1, e2 in zip(v1, v2)]
[1,3,5,6,8,7,3,3,2,3,4,5]
print(vector_add(a, b))

