x=(12)

## Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(x))

## Example 2: Using recursion

def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print (fibR(x))


def fib(n):
 a1 = 0
 a2 = 1
 for i in range (n):
   a1, a2= a2, a1+a2
 return x

print(fib(10))


#recursion

def fib(n):
 a1=2
 a2=1
 if n==0:
  return a1
 if n==1:
  return a2
 return fib(n-2) + fib (n-1)

print (fib(3))


d={}

def fib(n):
 a1=2
 a2=1
 if n==0:
  return a1
 if n==1:
  return a2
 if n in d:  return d[n]
 return fib(n-2) + fib (n-1)
 d[n]=res
 return res

print (fib(10))

#xcode-select -- install