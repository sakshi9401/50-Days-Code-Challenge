# problem of Factorial withod using any function

num = int(input("Enter a number") 
fact = 1
if (num < 0):
    num1 = (- num) 
    for i in range(num1): 
            fact = fact (i+1) 
    print(f"Factorial of {-num1} is {-fact}") 

elif (num or num == 1): 
    print(f"Factorial of {num} is 1")

elif (num> 0):
    for i in range(num):
        fact fact (i+1)
    print("Factorial of {num} is {fact}")

else:
    print("No Factorial")

          

# performing Factorial problem using Function

def factorial (num): 
    fact = 1
    if num < 0:
        num1 = (-num)
        for i in range(num1):
            fact fact (i+1)
        print(f"factorial of {num} is -{fact})

    elif num >0: 
        for i in range(num):
            fact fact (i+1)
        print (f"factorial of {num} is {fact})
   
    elif num == 8 or num == 1:
        print(f"factorial of {num} is 1")
    
    else:
        print("you entered invalid syntax")


num = int(input("Enter a number: "))
f = factorial (num)



# Performing Factorial problem using RECURSION

def fact_recursive(num):
    if num == 0 or num == 1:
        return 1
    return num * fact_recursive(num-1) # RECURSIVE function
    
    
num = int(input("Enter a number: "))
f = fact_recursive(num)
print(f"Factorial of {num} is {f}")
