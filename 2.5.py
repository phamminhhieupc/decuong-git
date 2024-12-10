def hpt(a1, b1, c1, a2, b2, c2):
    tg = a1 * b2 - a2 * b1
    if tg != 0:
        x = (c1 * b2 - c2 * b1) / tg
        y = (a1 * c2 - a2 * c1) / tg
        return f"x = {x}, y = {y}"
    else:
        if (a1 == 0 and b1 == 0 and c1 == 0) and (a2 == 0 and b2 == 0 and c2 == 0):
            return "vsn"
        elif (a1 / a2 == b1 / b2 == c1 / c2):
            return "vsn"
        else:
            return "vn"
a1,b1,c1 = map(float,input().split())
a2,b2,c2 = map(float,input().split())
kq = hpt(a1, b1, c1, a2, b2, c2)
print(kq)