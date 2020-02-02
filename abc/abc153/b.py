h, n = list(map(int,input().split()))
a = list(map(int,input().split()))
hit = sum(a)
if hit >= h:
    print("Yes")
else:
    print("No")