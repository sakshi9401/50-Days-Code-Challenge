print("Enter the Number: ", end="")
num = int(input())

temp = num
numLen = 0
while temp>0:
  numLen = numLen+1
  temp = int(temp/10)

if numLen>=4:
  numLen = int(numLen/2)
  chk = 0
  while num>0:
    rem = num%10
    if chk==numLen:
      midOne = rem
    elif chk==(numLen-1):
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  product = midOne*midTwo
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", product)
else:
  print("\nIt's not a 4 or more than 4-digit number!")
