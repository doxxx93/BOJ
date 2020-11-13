num =n = int(input())
count =0
while True:
    a= int(num//10)
    
    b = int(num%10)
    
    num = a+b
    count +=1  
    num = int(f"{b}{num%10}")
    
    if num == n:
        break
print(count)