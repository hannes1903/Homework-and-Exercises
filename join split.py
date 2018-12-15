cool_string = "kjdfladkjfsaska"

print (cool_string.split("a"))

cool_string2 = "lk ldsj odjfo  "

print (cool_string2.split("\t"))

t="1    2"
print (t)

print (repr(t))

#does not work here as phc converts tabs into space

a=[1,3,4,6,7,8] #thats numbers (integer)

print ("_".join([str(i) for i in a])) #convert integer to string

#joining only works on lists where every element is string

print ("_".join([str(i) for i in a])) #convert integer to string