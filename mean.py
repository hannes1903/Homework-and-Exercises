import math

import statistics

# 3 statistic functions mean, median, mode, euclidium_disctance (v1, v2)

h = [1,3,5,6,8,7,3,3,2,3,4,5,8]

x = statistics.mean(h)
y = statistics.median(h)

print(x)
print(y)

def mean_1(v):
    return statistics.mean(v)

print (mean_1(h))

def median_1(v):
    return statistics.median(v)

print (median_1(h))

####

b = [1,3,5,6,8,7,3,3,2,3,4,5,8]

def median(l):
    a=len(l)
    #odd
    if a%2==0:
        s_l = sorted(l)
        return mean_1([s_l[a//2], s_l[a//2-1]])
    #even
    else:
        return sorted(l)[a//2]

print ("median", median(b))

####

h = [1,3,5,6,8,7,3,3,2,3,4,5,8]

def median(l):
    a=len(l)
    if a==0:
        raise Exception ("list is empty")
    elif a==1:
        return l[0]
    s_l = sorted(l)
    if a%2==0:
        return (s_l[a//2] + s_l[a//2-1])/2
    else:
        return s_l[a//2]

print ("median", median(h))

# // rounds down, same as int(a/2)
# traceback






