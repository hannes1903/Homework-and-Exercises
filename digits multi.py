from functools import reduce

# returning the product of a list

h = [1,2,3,4,4,5]

print (reduce(lambda x, y: x * y, h, 1))


###

q= 123456

print (reduce(lambda x, y: x*y, (int(c) for c in str(q) if c !="0"), 1))
