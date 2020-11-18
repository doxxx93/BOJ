n = int(input())
f = [0,1]
if n < 2:
    print(f[n])
else:
    for i in range(n-1):
        f.append(f[-1]+f[-2])
    print(f[-1])