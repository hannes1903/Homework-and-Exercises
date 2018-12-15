import math
from typing import List


a=5
b=3
c=3


#List = [1,4,5]

def checkio(a: int, b: int, c: int) -> List[int]:
    if a + b <= c or b + c <= a or c +  a <= b:
        return [0, 0, 0]
    # C = Arccos ((a² + b² - c²) / 2ab)
    a1 = round(math.degrees(math.acos((b**2 + c**2 + a**2) / (2*b*c))))
    a2 = round(math.degrees(math.acos((a**2 + c**2 + b**2) / (2*a*c))))
    a3 = round(math.degrees(math.acos((a**2 + b**2 + c**2) / (2*a*b))))

    # replace this for solution
    return sorted ([a1, a2, a3])


print (checkio(a, b, c))










#C = Arccos ((a² + b² - c²) / 2ab)
#a= math.degrees(math.acos((b+c-a)/2*b*c))
#b= math.degrees(math.acos((b+c-a)/2*b*c))
#c= math.degrees(math.acos((b+c-a)/2*b*c))