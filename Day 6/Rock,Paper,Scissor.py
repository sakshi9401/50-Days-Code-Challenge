#Game of Rock ,Paper and Scissor 
import random

def winner(comp,your_choice):
    if comp == your_choice:
        return None
    elif comp == 'R':
        if your_choice == 'S':
            return 0
        elif your_choice == 'P':
            return 1
    elif comp == 'P':
        if your_choice == 'R':
            return 0
        elif your_choice == 'S':
            return 1
    elif comp == 'S':
        if your_choice == 'P':
            return 0
        elif your_choice == 'R':
            return 1
    

print("Let's play Rock , Paper and Scissor")
print("It's computer turn")
rand_num = random.randint(1,3)
if rand_num == 1:
    comp = 'R'
elif rand_num == 2:
    comp = 'P'
elif rand_num == 3:
    comp = 'S'
    
print("It's your turn now :")
print("\n\tEnter 'R' for Rock")
print("\n\tEnter 'P' for Paper")
print("\n\tEnter 'S' for Scissor")
your_choice = input()

print(f"You choose {your_choice}")
print(f"Computer choose {comp}")
    
W = winner(comp,your_choice)    
if W == None:
    print("Their is a tie between you and computer")
elif W:
    print("You win!!!!")
else:
    print("You Loose")
