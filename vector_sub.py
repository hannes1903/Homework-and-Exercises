import math
import statistics

v1=[3, 5, 1]
v2=[6, 1, 8]



def vector_sub(v1, v2):
    return [e1 - e2 for e1, e2 in zip(v1, v2)]

print(vector_sub(v1, v2))

v=[1,4,5,7,]
s=3

def scalar_mul(v, s):
    return [e*s for e in v]

print(scalar_mul(v, s))


a=[1, 2, 3]
b=[4, 5, 6]

#sum of elementwise multiplications

def dot(v1, v2):
    return sum([e1 * e2 for e1, e2 in zip(v1, v2)])

print (dot(a, b))

##
def magnitude(y):
    return math.sqrt(dot(v, v))

print (magnitude(a))

# 3 statistic functions mean, median, mode, euclidium_disctance (v1, v2)

h = [1,3,5,6,8]

x = statistics.mean(h)

print(x)

