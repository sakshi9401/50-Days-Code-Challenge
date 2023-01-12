import random
n = random.randrange(1,10)
guess = int(input("Guess the number: "))
while n!= guess:
    if guess < n:
        print("Guess heigher value")
        guess = int(input("Try again: "))
    elif guess > n:
        print("Guess lower value")
        guess = int(input("Try again: "))
    else:
      break
print("you guessed it right!!")
