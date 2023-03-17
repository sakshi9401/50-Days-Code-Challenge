def Armstrong(n):
    l = len(str(n))
    sum = 0
    n1 = int(n)
    while(n1!=0):
        r = n1 % 10
        sum = sum + (r**l)
        n1 = n1 // 10
    
    return (n == sum)

n = int(input())

if Armstrong(n):
    print(f"{n} is Armstrong")
else:
    print("Not Armstrong")
