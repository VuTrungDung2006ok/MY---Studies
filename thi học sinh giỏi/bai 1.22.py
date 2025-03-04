a = int(input())
n = list(map(int,input().split()))
while len(n) > a:
    n = list(map(int,input().split()))
for i in range(1,101):
    b = True
    for k in n:
        if i% k != 0:
            b = False
            break
    if b:
        for j in range(1, 101):
            j**=2
            if j % i ==0:
                print(j(0))