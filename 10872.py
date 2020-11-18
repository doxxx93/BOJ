n = int(input())
fac = 1
if n==0:
    print(fac)
else:
    for i in range(n):
        fac = fac * (i+1)
    print(fac)