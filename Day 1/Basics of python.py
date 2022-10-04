# performing basic Arithmetic operations
n1 = int(input("Enter number one"))
n2 = int(input("Enter number two"))
print(f"sum of {n1} and {n2} is " ,(n1)+(n2) )# using f'string
print(f"multiplication of {n1} and {n2} is" ,(n1) * (n2))
print(f"division of {n1} and {n2} is",(n1) / (n2))
print(f"modulus of {n1} and  {n2} is",(n1) % (n2))


#we can directly add 10 or any number to a variable
print(f"sum after adding 10 to {n1} is", n1+10)


#type function
var1 = 'hello'
var2 = 32
var3 = 36.7
print(type(var1)) # return <class str>
print(type(var2)) # retSurn <class int>
print(type(var3)) # return <class float>


#typecasting
var1 = "5" # string 5
var2 = "3" # string 3
print(int(var1) + int(var2)) #coverting string to integer


#string multiplication 
print(5 * "100 Day Code Challenge\n") #it will print 100 Day                                       Code Challenge 5 times
