a=[1,2,3,6,12]

b=[]
for i in a:
     b.append(i**2)

print ([b])

#  command slash or """   """

a=[1,4,9,36,144]
b=[i**2 for i in a]

print (b)

#for [] list, {} dictonary: mapping things / stores pairs

c={i:i**2 for i in a}
print (c)

b=(i**2 for i in a)
print (b)

for j in b:
    print(j)
