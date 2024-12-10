x,n = map(int,input().split())
S = 0  
for k in range(1, n + 1):  
    S += x ** k  

print(S)
