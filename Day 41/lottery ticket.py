n = int(input())
list =[]
for i in range(0,n):
   val = int(input())

   list.append(val)
#Lno = list(map(int, input().split()))
LT= int(input())
if LT in list:
    print(f"Lottery ticket {LT} is found at position {list.index(LT)+1}. Congrats! You won")
else:
    print("Sorry...ticket number doesn't match")