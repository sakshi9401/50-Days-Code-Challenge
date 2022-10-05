# Program to find whether the entered number is an Armstrong Number or not
# Taking input from user

num = int(input("Enter a number : "))

#Checking whether the entered number is negative or positive
if num < 0:    
    print("False, Negative Armstrong Number is not possible")
    
# If entered number is positive then go further
else:
    temp = num # storing original number to a temporary variable
    L = len(str(temp)) # Calculating length of a number
    sum = 0
    while num != 0:
        rem = num%10
        sum =  sum + (rem ** L) calculating and storing a number to a new variable sum 
        num = num//10
    
    if sum==temp: # checking if temp is equals to sum or not
        print(f"{temp} is an armstrong number")
    
    else:
        print(f"{temp} is not an armstrongg number")
