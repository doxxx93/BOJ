import sys
input = sys.stdin.readline
n = int(input())
a = [list(input().split()) for i in range(n)]
a.sort(key=lambda x: int(x[0]))
for i in a:
    print(i[0], i[1])
