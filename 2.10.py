import math 
x,n = map(int,input().split())
S = x
for k in range(n-1):  
    S = math.sqrt(x + S)  
print(S)
