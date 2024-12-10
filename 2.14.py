import math
a = float(input())  
n = 1 
S = 1 
while 1 / math.factorial(2 * n + 1) > a:  
    S += 1 / math.factorial(2 * n + 1)
    n += 1  
print(S)
