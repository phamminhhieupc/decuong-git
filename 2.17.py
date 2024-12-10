import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
CA = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
if AB + BC > CA and AB + CA > BC and BC + CA > AB:
    P = AB + BC + CA
    print(P)
    p = P / 2
    S = math.sqrt(p * (p - AB) * (p - BC) * (p - CA))
    print(S)
else:
    print("khong la tam giac")
