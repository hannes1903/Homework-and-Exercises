#def func(*args):
#   return (max(args)-min(args)
#            if args else 0)

#print (func (100, 9))


###range, how to get a list of numbers in the power of three, where the numbers are in the range 10-100 and to to be deided by 7

a=[]

for n in range (10, 100):
    if n % 7 == 0:
        a.append(n**3)

print (a)

# % reminder
# == comparison, true and false
# append = method

### list comprehension

b = [n**3 for n in range (10, 101) if n % 7 ==0]

print (b)

c = [n**3 for n in range (14, 101, 7)]

print(c)

c = (n**3 for n in range (14, 101, 7))

print(c)

for j in a:numbers
    print (j)

list (a)

print (a)

# a=5
# lst=[]
# method tied to an object, lst.append ()   range ()
# len (lst), but can linked to other objects
# len(range(1, 10)
# builtin function eg sorted ()


# import random
# random random (10)

# l=[]      list
# d={}      dictonary
# t=()      tuple (list w/o methods), immutable types
# s=set()   set
# def func
  #  a=1
  #  b=2
# return a, b

# x1, x2 = Func ()
