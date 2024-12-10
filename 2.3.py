import math  

def pt2(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)  
    elif delta == 0:
        x = -b / (2*a)
        return (x) 

a,b,c = map(float,input().split())
if b**2 - 4*a*c >= 0:
    nghiem = pt2(a, b, c)
    print(nghiem)
else:
    print("vn")