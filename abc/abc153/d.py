h = int(input())
cnt = 0
i = 0
while h > 0:
    h = h//2
    cnt += 1*(2**i)
    i += 1
print(cnt)