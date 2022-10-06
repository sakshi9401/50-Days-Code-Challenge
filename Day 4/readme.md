# Topic : Check whether the number is prime or composite

## Language Used : Python Programming Language

### Explanation :  A number that is divisible only by itself and 1
                  Eg., 2, 3, 5, and so on..
                  
### Logic : 
           step 1 : input any number
           step 2 : check if it is 0 or 1 ,if yes then print 0 and 1 neither prime nor composite.
           step 3 : check if number is -ve or not, if it is negative then print there is no negative prime number
           step 4 : check if number is +ve, then check for prime number 
                     
### Code : num = take input from user
           i is for performing iterations in range(2 to num)
            if num % i == 0:
               return false
            if False:
               print number is prime
            else :
               print number is composite
                        
### Test Case 1: num = 0
                 0 neither prime nor composite.
                
### Test Case 2: num = 1
                 1 neither prime nor composite.             
                 
### Test Case 3: num = -5
                 Negative integer can not be prime.
                 
### Test Case 4: num = 2
                 2 is prime number
                 
### Test Case 5: num = 7
                 7 is prime number
                 
### Test Case 6: num = 8
                 8 is composite number
