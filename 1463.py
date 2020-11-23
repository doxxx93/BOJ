n = int(input())
number = n
count = 0

def cal(n, count):
    if n % 3 == 0 and n % 2 == 0:
        n = n//3
        
        count += 1
    elif n % 3 != 0 and n % 2 == 0:
        n == n//2
        count += 1
    elif n % 3 == 0 and n % 2 != 0:
        n == n//3
        count += 1
    else:
        n -= 1
        count += 1


while n ==1 :
    cal(n, count)
    print(n)
    print(count)



