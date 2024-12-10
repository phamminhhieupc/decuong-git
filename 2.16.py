import math
a,b,c = map(float,input().split())
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh này tạo thành một tam giác.")
    P = a + b + c
    print(P)
    P = P / 2 
    S = math.sqrt(P * (P - a) * (P - b) * (P - c))
    print(S)
else:
    print("khong la tam giac")
