import math
x,ep = map(float,input().split())
n = 0
term = 1  
S = 1     
while term >= ep:
    n += 1
    term = (x ** n) / math.factorial(n)  
    S += term
print(S)
