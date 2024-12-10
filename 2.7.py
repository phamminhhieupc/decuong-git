s=0
n = int(input())
for k in range(1, n + 1):  
    s += 1 / (k * (k + 1))
print(s)
