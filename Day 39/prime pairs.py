def prime(n):
          flag = False
          if n == 0:
                    return False
          elif n == 1:
                    return True
          elif n==2:
                    return True
          elif n > 1:
    
                    for i in range(2, n):
                              if (n % i) == 0:
                                        flag = True
                                        break
                    if flag:
                              return False
                    else:
                              return True
x = int(input())
n = int(input())
m = int(input())
c = 0
for i in range(n,m+1):
          if (prime(i) and prime(i+x)):
                    print(f"({i}, {i+x})")
                    c = c+1
print(f"Total number of pairs are {c}")
