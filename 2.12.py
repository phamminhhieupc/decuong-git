import math
n = int(input())
S = 0  
for k in range(0, n + 1):
    x = 2 * k + 1
    S += math.factorial(x)  
print(S)
