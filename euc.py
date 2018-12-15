# euclidium distance
import math

x=[3, 5, 1]
y=[6, 1, 8]


distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

print("Euclidean distance from x to y: ",distance)

# euclidium distance with function

def euc(t, s):
    return (math.sqrt(sum([(a - b) ** 2 for a, b in zip(t, s)])))

print("Euclidean distance from x to y: ", euc(x, y))