n = int(input())
d = 0
socan = int(n**(1/2))
for i in range(1, socan+1):
    if n % i ==0:
        d+=2

if socan * socan == n:
    d-=1

print(d)