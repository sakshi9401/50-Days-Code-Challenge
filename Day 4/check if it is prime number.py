num = (input("Enter a number"))
prime = True
n = int(num)
if(n==0 or n==1):
    print(f"{num} is neither Prime nor Composite")
    
elif (n < 0):
    print(f"Since, {num} is negative.\nHence, negative integers can not be prime.")
    
elif n > 0:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if(prime == False):
        print(f"{num} is Composite Number")
        
    else:
        print(f"{num} is Prime Number")
        
else:
    print(f"{num} is an invalid input")
