def main():
    n = int(input())
    if n % 5 == 0:
        print(int(n/5))
    else:
        a = 0
        while True:
            n -= 3
            if n < 0:
                print(-1)
                break
            a +=1
            if n % 5 ==0:
                a += n/5
                print(int(a))
                break
                
if __name__ == "__main__":
    main()