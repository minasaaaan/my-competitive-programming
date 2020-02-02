h, n = list(map(int,input().split()))
mahou = []
for i in range(n):
    a, b = list(map(int,input().split()))
    mahou.append([a,b])
dp=[100000000000]*(h+100000)
dp[h] = 0
for i in range(h):
    for j in range(n):
        damage = mahou[j][0]
        mp = mahou[j][1]
        hp = h-i
        if dp[hp - damage] > dp[hp] + mp:
            dp[hp - damage] = dp[hp] + mp
dp.append(dp[0])
dp = dp[h+1:]

print(min(dp))