x = 0
y = 0
x0 = list(map(int, input().split(" ")))
x1 = list(map(int, input().split(" ")))
x2 = list(map(int, input().split(" ")))

if x0[0] == x1[0]:
    x = x2[0]
elif x0[0] == x2[0]:
    x = x1[0]
else:
    x = x0[0]

if x0[1] == x1[1]:
    y = x2[1]
elif x0[1] == x2[1]:
    y = x1[1]
else:
    y = x0[1]

print(x, y)
