n, k = list(map(int,input().split()))
h = sorted(list(map(int,input().split())),reverse = True)
h = h[k:]
if n >= k:
    print(sum(h))
else:
    print(0)