import math
n = int(input())
S = 0  
for k in range(1, n + 1):
    S += math.factorial(k)  
print(S)
