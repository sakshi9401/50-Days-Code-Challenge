import random
passlen = int(input("Enter the length of password "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"
p = "".join(random.sample(s,passlen))
print(f"Random Password is {p}")
