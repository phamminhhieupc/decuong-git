a,b = map(int,input().split())
if a==0:
    if b==0:
        print("vsn")
    else:
        print("vn")
    
else:
    n = -b/a
    print(n)
