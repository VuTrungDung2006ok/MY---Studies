import math
n = int(input())
s = 0
for i in range(n+1):
    s += i**3
    m = math.sqrt(s)

print(round(m))
