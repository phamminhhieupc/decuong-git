a,b = map(int,input().split())
if a==0:
    if b>0:
        print("vsn")
    else:
        print("vn")   
else:
    if a<0:
        print("x < ",-b/a)
    else:
        print("x > ",-b/a)
