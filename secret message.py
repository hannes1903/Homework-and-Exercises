
s = "lkd KLS jMkl"

def find_message(s):
     result=[]
     for c in s:
          if c.isupper():
               result.append(c)
     return "".join(result)

print (find_message(s))


print ("".join(c for c in s if c.upper()))

#find_message2 = lambda s: "".join((c for c in s if c.upper())))

