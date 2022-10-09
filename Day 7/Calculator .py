#Calculator using oops concept with some operations:
1- Addition, 2- Subtraction, 3- Multiplication, 4- Division, 5- Modulus, 6- Square, 7-Square Root, 8- Cube, 9- Cube Root

class Calculator:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
    def addition(self):
        print(f"Addition of {self.num1} and {self.num2} is {self.num1 + self.num2}")
    def subtraction(self):
        print(f"Subtraction of {self.num1} and {self.num2} is {self.num1 - self.num2}")
    def multiplication(self):
        print(f"Multiplication of {self.num1} and {self.num2} is {self.num1 * self.num2}")
    def division(self):
        print(f"Division of {self.num1} and {self.num2} is {self.num1 // self.num2}")
    def modulus(self):
        print(f"Modulus of {self.num1} and {self.num2} is {self.num1 % self.num2}")
    def square(self):
        print(f"Square of {self.num1} is {self.num1**2}")
    def squareRoot(self):
        print(f"Square Root of {self.num1} is {self.num1** 0.5}")
    def cube(self):
        print(f"Cube of {self.num1} is {self.num1**3}")
    def cubeRoot(self):
        print(f"Cube Root of {self.num1} is {self.num1**0.33}")
    
n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
choice = int(input("Enter your choice :\n1 for Addition\n2 for subtraction\n3 for Multiplication\
                    \n4 for Division \n5 for Modulus\n6 for Square\n7 for Square Root\
                    \n8 for Cube\n9 for Cube Root\n"))
print(f"you choose {choice}")
num = Calculator(n1,n2)
if choice==1:
    num.addition()
elif choice==2:
    num.subtraction()
elif choice==3:
    num.multiplication()
elif choice==4:
    num.division()
elif choice==5:
    num.modulus()
elif choice==6:
    num.square()
elif choice==7:
    num.squareRoot()
elif choice==8:
    num.cube()
elif choice==9:
    num.cubeRoot()

















